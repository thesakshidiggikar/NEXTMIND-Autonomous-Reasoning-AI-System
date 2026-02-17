import './style.css'

document.addEventListener('DOMContentLoaded', () => {
  // Intersection Observer for scroll animations
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Apply reveal animation to cards and sections
  const revealElements = document.querySelectorAll('.card, section .section-title, .diagram-container, pre');
  revealElements.forEach(el => {
    el.classList.add('reveal');
    observer.observe(el);
  });

  // Simple smooth scroll for nav links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      e.preventDefault();
      const href = anchor.getAttribute('href');
      const targetId = href ? href.substring(1) : null;
      if (targetId) {
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
          window.scrollTo({
            top: targetElement.offsetTop - 80, // Account for header
            behavior: 'smooth'
          });
        }
      }
    });
  });

  // Animated path for SVG diagram
  const svgLines = document.querySelectorAll('.architecture-svg path');
  svgLines.forEach((line) => {
    const pathLine = line as SVGPathElement;
    const length = pathLine.getTotalLength();
    pathLine.style.strokeDasharray = length.toString();
    pathLine.style.strokeDashoffset = length.toString();
    pathLine.style.animation = 'draw 2s ease-out forwards';
  });
  // Simulator Logic
  const uncertaintyInput = document.getElementById('uncertainty') as HTMLInputElement;
  const noveltyInput = document.getElementById('novelty') as HTMLInputElement;
  const uncertaintyVal = document.getElementById('uncertainty-val');
  const noveltyVal = document.getElementById('novelty-val');
  const runBtn = document.getElementById('run-btn') as HTMLButtonElement;
  const outputLog = document.getElementById('output-log');
  const steps = document.querySelectorAll('.step');

  const updateDisplay = (input: HTMLInputElement, display: HTMLElement | null) => {
    if (display) display.textContent = (parseInt(input.value) / 100).toFixed(2);
  };

  uncertaintyInput?.addEventListener('input', () => updateDisplay(uncertaintyInput, uncertaintyVal));
  noveltyInput?.addEventListener('input', () => updateDisplay(noveltyInput, noveltyVal));

  const addLog = (message: string, type: 'info' | 'success' | 'highlight' = 'info') => {
    if (outputLog) {
      const entry = document.createElement('div');
      entry.className = `log-entry ${type}`;
      entry.innerHTML = `<span class="prompt">> </span>${message}`;
      outputLog.appendChild(entry);
      outputLog.scrollTop = outputLog.scrollHeight;
    }
  };

  const sleep = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

  runBtn?.addEventListener('click', async () => {
    runBtn.disabled = true;
    if (outputLog) outputLog.innerHTML = '';
    steps.forEach(s => s.classList.remove('active'));

    const u = parseFloat(uncertaintyVal?.textContent || '0');
    const n = parseFloat(noveltyVal?.textContent || '0');

    // Step 1: Processing
    steps[0].classList.add('active');
    addLog(`Initializing pipeline with uncertainty=${u}, novelty=${n}`, 'info');
    await sleep(800);
    addLog('Signal weights computed.', 'success');
    await sleep(400);

    // Step 2: Curiosity
    steps[1].classList.add('active');
    addLog('Querying Curiosity Engine...', 'info');
    await sleep(1200);
    const score = ((u * 0.7) + (n * 0.3)).toFixed(2);
    addLog(`Curiosity Score: ${score}`, 'highlight');
    await sleep(400);

    // Step 3: Reasoning
    steps[2].classList.add('active');
    addLog('Invoking local LLM (llm-hypothesis-v1)...', 'info');
    await sleep(2000);
    addLog('Internal reasoning completed.', 'success');
    await sleep(400);

    // Step 4: Meta-Control
    steps[3].classList.add('active');
    addLog('Evaluating with Meta-Controller...', 'info');
    await sleep(1000);
    const decision = parseFloat(score) > 0.5 ? 'EXPLORE' : 'STABILIZE';
    addLog(`Meta Decision: ${decision}`, 'highlight');

    await sleep(600);
    addLog('Pipeline execution finished.', 'success');
    runBtn.disabled = false;
  });
});

// Animation styles
const style = document.createElement('style');
style.innerHTML = `
  .reveal {
    opacity: 0;
    transform: translateY(30px);
    transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .reveal.visible {
    opacity: 1;
    transform: translateY(0);
  }
  @keyframes draw {
    to {
      stroke-dashoffset: 0;
    }
  }
`;
document.head.appendChild(style);
