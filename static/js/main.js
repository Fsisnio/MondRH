// MonDRH - Main JavaScript File

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initNavbar();
    initContactForm();
    initAnimations();
    initSmoothScrolling();
    initHomepageEnhancements(); // Nouvelle fonction
    initCounterAnimations(); // Nouvelle fonction
    initScrollIndicator(); // Nouvelle fonction
    initParallaxEffects(); // Nouvelle fonction
});

// Navbar functionality
function initNavbar() {
    const navbar = document.querySelector('.navbar');
    
    // Add scroll effect to navbar
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('shadow-sm');
        } else {
            navbar.classList.remove('shadow-sm');
        }
    });
    
    // Close mobile menu when clicking on a link
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (navbarCollapse.classList.contains('show')) {
                const bsCollapse = new bootstrap.Collapse(navbarCollapse);
                bsCollapse.hide();
            }
        });
    });
}

// Contact form functionality
function initContactForm() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = {
                firstName: document.getElementById('firstName').value,
                lastName: document.getElementById('lastName').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                company: document.getElementById('company').value,
                service: document.getElementById('service').value,
                message: document.getElementById('message').value
            };
            
            // Validate form
            if (!validateForm(formData)) {
                return;
            }
            
            // Show loading state
            const submitBtn = contactForm.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Envoi en cours...';
            submitBtn.disabled = true;
            
            // Send form data
            fetch('/api/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                showAlert('success', 'Message envoyé avec succès ! Nous vous recontacterons rapidement.');
                contactForm.reset();
            })
            .catch(error => {
                console.error('Error:', error);
                showAlert('danger', 'Une erreur est survenue. Veuillez réessayer.');
            })
            .finally(() => {
                // Reset button state
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            });
        });
    }
}

// Form validation
function validateForm(data) {
    const requiredFields = ['firstName', 'lastName', 'email', 'message'];
    
    for (let field of requiredFields) {
        if (!data[field] || data[field].trim() === '') {
            showAlert('danger', `Le champ ${getFieldLabel(field)} est requis.`);
            return false;
        }
    }
    
    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(data.email)) {
        showAlert('danger', 'Veuillez entrer une adresse email valide.');
        return false;
    }
    
    return true;
}

// Get field label
function getFieldLabel(field) {
    const labels = {
        firstName: 'Prénom',
        lastName: 'Nom',
        email: 'Email',
        phone: 'Téléphone',
        company: 'Entreprise',
        service: 'Service',
        message: 'Message'
    };
    return labels[field] || field;
}

// Show alert
function showAlert(type, message) {
    const alertContainer = document.createElement('div');
    alertContainer.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    alertContainer.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    alertContainer.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(alertContainer);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (alertContainer.parentNode) {
            alertContainer.remove();
        }
    }, 5000);
}

// Animations
function initAnimations() {
    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animateElements = document.querySelectorAll('.solution-card, .team-card, .number-card, .growth-item');
    animateElements.forEach(el => observer.observe(el));
}

// Smooth scrolling
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                const offsetTop = targetElement.offsetTop - 80; // Account for fixed navbar
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// ===== NOUVELLES FONCTIONNALITÉS POUR LA PAGE D'ACCUEIL AMÉLIORÉE =====

// Améliorations de la page d'accueil
function initHomepageEnhancements() {
    // Effet de parallaxe sur les sections
    initParallaxSections();
    
    // Animations des cartes au survol
    initCardHoverEffects();
    
    // Effet de particules interactives
    initParticleEffects();
    
    // Animations des boutons
    initButtonAnimations();
    
    // Effet de glassmorphism
    initGlassmorphismEffects();
}

// Animations des compteurs
function initCounterAnimations() {
    const counters = document.querySelectorAll('.counter');
    
    const counterObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = parseInt(counter.getAttribute('data-target'));
                const duration = 2000; // 2 secondes
                const increment = target / (duration / 16); // 60 FPS
        let current = 0;
        
        const updateCounter = () => {
                current += increment;
                    if (current < target) {
                        counter.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                        counter.textContent = target;
            }
        };
        
        updateCounter();
                counterObserver.unobserve(counter);
            }
        });
    }, { threshold: 0.5 });
    
    counters.forEach(counter => counterObserver.observe(counter));
}

// Indicateur de défilement
function initScrollIndicator() {
    const scrollIndicator = document.querySelector('.scroll-arrow');
    
    if (scrollIndicator) {
        scrollIndicator.addEventListener('click', function() {
            const servicesSection = document.getElementById('services');
            if (servicesSection) {
                servicesSection.scrollIntoView({ behavior: 'smooth' });
            }
        });
        
        // Masquer l'indicateur après le premier scroll
        window.addEventListener('scroll', function() {
            if (window.scrollY > 100) {
                scrollIndicator.style.opacity = '0';
                scrollIndicator.style.pointerEvents = 'none';
            } else {
                scrollIndicator.style.opacity = '1';
                scrollIndicator.style.pointerEvents = 'auto';
            }
        });
    }
}

// Effets de parallaxe
function initParallaxEffects() {
    const parallaxElements = document.querySelectorAll('.hero-bg-pattern, .section-bg-pattern, .growth-bg-pattern');
    
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        
        parallaxElements.forEach(element => {
            const speed = 0.5;
            const yPos = -(scrolled * speed);
            element.style.transform = `translateY(${yPos}px)`;
        });
    });
}

// Effet de parallaxe sur les sections
function initParallaxSections() {
    const sections = document.querySelectorAll('section');
    
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        
        sections.forEach(section => {
            const speed = 0.1;
            const yPos = -(scrolled * speed);
            const bgPattern = section.querySelector('.section-bg-pattern, .growth-bg-pattern, .numbers-bg-pattern');
            
            if (bgPattern) {
                bgPattern.style.transform = `translateY(${yPos}px)`;
            }
        });
    });
}

// Effets de survol des cartes
function initCardHoverEffects() {
    const cards = document.querySelectorAll('.solution-card, .team-card, .number-card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
}

// Effets de particules
function initParticleEffects() {
    const heroSection = document.querySelector('.hero-section');
    
    if (heroSection) {
        // Créer des particules dynamiques
        for (let i = 0; i < 20; i++) {
            createParticle(heroSection);
        }
    }
}

function createParticle(container) {
    const particle = document.createElement('div');
    particle.className = 'particle';
    particle.style.cssText = `
        position: absolute;
        width: 4px;
        height: 4px;
        background: rgba(255, 255, 255, 0.6);
        border-radius: 50%;
        pointer-events: none;
        animation: particleFloat 8s linear infinite;
    `;
    
    // Position aléatoire
    particle.style.left = Math.random() * 100 + '%';
    particle.style.top = Math.random() * 100 + '%';
    particle.style.animationDelay = Math.random() * 8 + 's';
    
    container.appendChild(particle);
}

// Animations des boutons
function initButtonAnimations() {
    const buttons = document.querySelectorAll('.hero-btn, .solution-btn, .contact-btn, .newsletter-btn');
    
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px) scale(1.05)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
        
        // Effet de clic
        button.addEventListener('click', function() {
            this.style.transform = 'translateY(0) scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'translateY(-3px) scale(1.05)';
            }, 150);
        });
    });
}

// Effets de glassmorphism
function initGlassmorphismEffects() {
    const glassElements = document.querySelectorAll('.stat-card, .floating-card, .number-card');
    
    glassElements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            this.style.backdropFilter = 'blur(20px)';
            this.style.backgroundColor = 'rgba(255, 255, 255, 0.2)';
        });
        
        element.addEventListener('mouseleave', function() {
            this.style.backdropFilter = 'blur(10px)';
            this.style.backgroundColor = 'rgba(255, 255, 255, 0.1)';
        });
    });
}

// Amélioration des formulaires
function enhanceForms() {
    const inputs = document.querySelectorAll('input, textarea, select');
    
    inputs.forEach(input => {
        // Effet de focus
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        
        input.addEventListener('blur', function() {
            if (!this.value) {
                this.parentElement.classList.remove('focused');
            }
        });
        
        // Animation de remplissage
        if (input.value) {
            input.parentElement.classList.add('focused');
        }
    });
}

// Effet de loading pour les boutons
function initLoadingStates() {
    const buttons = document.querySelectorAll('button[type="submit"]');
    
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            if (!this.disabled) {
                this.classList.add('loading');
                this.disabled = true;
                
                // Simuler un délai (à remplacer par la vraie logique)
                setTimeout(() => {
                    this.classList.remove('loading');
                    this.disabled = false;
                }, 2000);
            }
        });
    });
}

// Animations d'entrée pour les sections
function initSectionAnimations() {
    const sections = document.querySelectorAll('section');
    
    const sectionObserver = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
                entry.target.classList.add('section-visible');
                
                // Animer les éléments enfants
                const animatedElements = entry.target.querySelectorAll('.animate-on-scroll');
                animatedElements.forEach((el, index) => {
                    setTimeout(() => {
                        el.classList.add('animate-in');
                    }, index * 100);
                });
        }
    });
    }, { threshold: 0.2 });

    sections.forEach(section => sectionObserver.observe(section));
}

// Effet de texte animé
function initTextAnimations() {
    const animatedTexts = document.querySelectorAll('.gradient-text');
    
    animatedTexts.forEach(text => {
        // Effet de typewriter
        const originalText = text.textContent;
        text.textContent = '';
        let i = 0;
        
        function typeWriter() {
            if (i < originalText.length) {
                text.textContent += originalText.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        }
        
        // Démarrer l'animation quand l'élément est visible
        const textObserver = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    typeWriter();
                    textObserver.unobserve(entry.target);
                }
            });
        });
        
        textObserver.observe(text);
    });
}

// Initialisation des améliorations au chargement
document.addEventListener('DOMContentLoaded', function() {
    enhanceForms();
    initLoadingStates();
    initSectionAnimations();
    initTextAnimations();
});

// CSS pour les nouvelles animations
const newStyles = `
    @keyframes particleFloat {
        0% {
            transform: translateY(100vh) rotate(0deg);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            transform: translateY(-100px) rotate(360deg);
            opacity: 0;
        }
    }
    
    .section-visible {
        animation: fadeInUp 0.8s ease-out;
    }
    
    .animate-on-scroll {
        opacity: 0;
        transform: translateY(30px);
        transition: all 0.6s ease-out;
    }
    
    .animate-on-scroll.animate-in {
        opacity: 1;
        transform: translateY(0);
    }
    
    .focused {
        transform: translateY(-2px);
    }
    
    .focused input,
    .focused textarea,
    .focused select {
        border-color: var(--primary-color);
        box-shadow: 0 0 0 0.2rem rgba(13, 110, 253, 0.25);
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;

// Ajouter les styles au document
const styleSheet = document.createElement('style');
styleSheet.textContent = newStyles;
document.head.appendChild(styleSheet);

// Service card hover effects
document.addEventListener('DOMContentLoaded', function() {
    const serviceCards = document.querySelectorAll('.service-card');
    
    serviceCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});

// Mobile menu improvements
document.addEventListener('DOMContentLoaded', function() {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    if (navbarToggler && navbarCollapse) {
        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!navbarToggler.contains(e.target) && !navbarCollapse.contains(e.target)) {
                if (navbarCollapse.classList.contains('show')) {
                    const bsCollapse = new bootstrap.Collapse(navbarCollapse);
                    bsCollapse.hide();
                }
            }
        });
    }
});

// Lazy loading for images (if any are added later)
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// Initialize lazy loading
initLazyLoading();

// Performance optimization: Debounce scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Apply debouncing to scroll events
window.addEventListener('scroll', debounce(function() {
    // Any scroll-based functionality can be added here
}, 10));

// Chat functionality
function initChat() {
    const chatToggle = document.getElementById('chat-toggle');
    const chatContainer = document.getElementById('chat-container');
    const chatClose = document.getElementById('chat-close');
    const chatSend = document.getElementById('chat-send');
    const chatInput = document.getElementById('chat-input-field');
    const chatMessages = document.getElementById('chat-messages');

    if (!chatToggle) return;

    // Toggle chat
    chatToggle.addEventListener('click', function() {
        chatContainer.style.display = chatContainer.style.display === 'none' ? 'flex' : 'none';
    });

    // Close chat
    chatClose.addEventListener('click', function() {
        chatContainer.style.display = 'none';
    });

    // Send message
    function sendMessage() {
        const message = chatInput.value.trim();
        if (!message) return;

        // Add user message
        addMessage(message, 'user');
        chatInput.value = '';

        // Send to server
        fetch('/api/chat/message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            // Add bot response
            setTimeout(() => {
                addMessage(data.message, 'bot');
            }, 1000);
        })
        .catch(error => {
            console.error('Error:', error);
            addMessage('Désolé, une erreur est survenue. Veuillez réessayer.', 'bot');
        });
    }

    // Add message to chat
    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const now = new Date();
        const time = now.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
        
        messageDiv.innerHTML = `
            <div class="message-content">${text}</div>
            <small class="message-time">${time}</small>
        `;
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Send on button click
    chatSend.addEventListener('click', sendMessage);

    // Send on Enter key
    chatInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
}

// LinkedIn integration
function initLinkedInIntegration() {
    // LinkedIn OAuth integration would go here
    // For now, we'll just show a placeholder
    console.log('LinkedIn integration ready');
}

// Newsletter functionality
function initNewsletter() {
    const newsletterForm = document.querySelector('form[action*="newsletter"]');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            const email = this.querySelector('input[type="email"]').value;
            if (!email) {
                e.preventDefault();
                alert('Veuillez entrer une adresse email valide.');
            }
        });
    }
}

// Initialisation des fonctionnalités
document.addEventListener('DOMContentLoaded', function() {
    initChat();
    initLinkedInIntegration();
    initNewsletter();
    initCounters();
    initScrollAnimations();
    initContactForm();
});

// Animation des compteurs
function initCounters() {
    const counters = document.querySelectorAll('.counter');
    
    const animateCounter = (counter) => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000; // 2 secondes
        const step = target / (duration / 16); // 60 FPS
        let current = 0;
        
        const timer = setInterval(() => {
            current += step;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            counter.textContent = Math.floor(current);
        }, 16);
    };
    
    // Observer pour déclencher l'animation quand visible
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    counters.forEach(counter => {
        observer.observe(counter);
    });
}

// Animations au scroll
function initScrollAnimations() {
    const elements = document.querySelectorAll('.solution-card, .team-card, .growth-item, .number-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('slide-up');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    
    elements.forEach(element => {
        observer.observe(element);
    });
}

// Chat Widget
function initChat() {
    const chatToggle = document.getElementById('chat-toggle');
    const chatContainer = document.getElementById('chat-container');
    const chatClose = document.getElementById('chat-close');
    const chatSend = document.getElementById('chat-send');
    const chatInput = document.getElementById('chat-input-field');
    const chatMessages = document.getElementById('chat-messages');

    if (!chatToggle || !chatContainer) return;

    // Toggle chat
    chatToggle.addEventListener('click', function() {
        chatContainer.style.display = chatContainer.style.display === 'none' ? 'flex' : 'none';
        if (chatContainer.style.display === 'flex') {
            chatInput.focus();
        }
    });

    // Close chat
    if (chatClose) {
        chatClose.addEventListener('click', function() {
            chatContainer.style.display = 'none';
        });
    }

    // Send message
    function sendMessage() {
        const message = chatInput.value.trim();
        if (!message) return;

        // Add user message
        addMessage(message, 'user');
        chatInput.value = '';

        // Simulate bot response
        setTimeout(() => {
            const responses = [
                "Merci pour votre message ! Un consultant vous répondra dans les plus brefs délais.",
                "Excellente question ! Laissez-moi vous connecter avec notre équipe spécialisée.",
                "Nous avons bien reçu votre demande. Un membre de notre équipe vous contactera rapidement.",
                "Parfait ! Notre équipe va analyser votre demande et vous proposer une solution adaptée."
            ];
            const randomResponse = responses[Math.floor(Math.random() * responses.length)];
            addMessage(randomResponse, 'bot');
        }, 1000);
    }

    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const now = new Date();
        const timeString = now.toLocaleTimeString('fr-FR', { 
            hour: '2-digit', 
            minute: '2-digit' 
        });
        
        messageDiv.innerHTML = `
            <div class="message-content">${text}</div>
            <small class="message-time">${timeString}</small>
        `;
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    if (chatSend) {
        chatSend.addEventListener('click', sendMessage);
    }

    if (chatInput) {
        chatInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    }
}

// LinkedIn Integration
function initLinkedInIntegration() {
    const linkedinButtons = document.querySelectorAll('.linkedin-import');
    
    linkedinButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Simulation de l'intégration LinkedIn
            const loadingText = 'Connexion à LinkedIn...';
            const originalText = button.innerHTML;
            
            button.innerHTML = `<i class="fas fa-spinner fa-spin me-2"></i>${loadingText}`;
            button.disabled = true;
            
            setTimeout(() => {
                // Simuler une réponse de l'API LinkedIn
                fetch('/api/linkedin-import', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        action: 'import_profile'
                    })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        button.innerHTML = '<i class="fas fa-check me-2"></i>Profil importé';
                        button.classList.remove('btn-outline-primary');
                        button.classList.add('btn-success');
                        
                        // Afficher les données importées
                        showLinkedInData(data.profile);
                    } else {
                        throw new Error(data.message || 'Erreur lors de l\'import');
                    }
                })
                .catch(error => {
                    console.error('Erreur LinkedIn:', error);
                    button.innerHTML = originalText;
                    button.disabled = false;
                    alert('Erreur lors de la connexion à LinkedIn. Veuillez réessayer.');
                });
            }, 2000);
        });
    });
}

function showLinkedInData(profile) {
    // Remplir automatiquement les champs du formulaire
    const fields = {
        'firstName': profile.firstName,
        'lastName': profile.lastName,
        'email': profile.email,
        'phone': profile.phone,
        'company': profile.company,
        'position': profile.position,
        'experience': profile.experience
    };
    
    Object.keys(fields).forEach(fieldId => {
        const field = document.getElementById(fieldId);
        if (field && fields[fieldId]) {
            field.value = fields[fieldId];
        }
    });
    
    // Afficher une notification
    showNotification('Profil LinkedIn importé avec succès !', 'success');
}

// Newsletter
function initNewsletter() {
    const newsletterForm = document.querySelector('form[action*="newsletter"]');
    
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            const emailField = this.querySelector('input[type="email"]');
            const firstNameField = this.querySelector('input[name="first_name"]');
            
            if (!emailField.value) {
                e.preventDefault();
                showNotification('Veuillez saisir votre adresse email.', 'error');
                return;
            }
            
            if (!isValidEmail(emailField.value)) {
                e.preventDefault();
                showNotification('Veuillez saisir une adresse email valide.', 'error');
                return;
            }
            
            // Animation de soumission
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Inscription...';
            submitBtn.disabled = true;
            
            // Simuler le traitement
            setTimeout(() => {
                submitBtn.innerHTML = '<i class="fas fa-check me-2"></i>Inscrit !';
                showNotification('Inscription à la newsletter réussie !', 'success');
            }, 1500);
        });
    }
}

// Contact Form
function initContactForm() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Validation des champs
            const requiredFields = ['firstName', 'lastName', 'email', 'message'];
            let isValid = true;
            
            requiredFields.forEach(fieldId => {
                const field = document.getElementById(fieldId);
                if (!field.value.trim()) {
                    field.classList.add('is-invalid');
                    isValid = false;
                } else {
                    field.classList.remove('is-invalid');
                }
            });
            
            if (!isValid) {
                showNotification('Veuillez remplir tous les champs obligatoires.', 'error');
                return;
            }
            
            if (!isValidEmail(document.getElementById('email').value)) {
                showNotification('Veuillez saisir une adresse email valide.', 'error');
                return;
            }
            
            // Animation de soumission
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Envoi en cours...';
            submitBtn.disabled = true;
            
            // Simuler l'envoi
            setTimeout(() => {
                submitBtn.innerHTML = '<i class="fas fa-check me-2"></i>Message envoyé !';
                showNotification('Votre message a été envoyé avec succès !', 'success');
                
                // Reset form
                setTimeout(() => {
                    contactForm.reset();
                    submitBtn.innerHTML = originalText;
                    submitBtn.disabled = false;
                }, 2000);
            }, 2000);
        });
    }
}

// Validation email
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Système de notifications
function showNotification(message, type = 'info') {
    // Créer la notification
    const notification = document.createElement('div');
    notification.className = `alert alert-${type === 'error' ? 'danger' : type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = `
        top: 20px;
        right: 20px;
        z-index: 9999;
        min-width: 300px;
        box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
        border: none;
        border-radius: 0.5rem;
    `;
    
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto-remove après 5 secondes
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

// Validation des fichiers CV
function validateCVFile(input) {
    const file = input.files[0];
    const maxSize = 16 * 1024 * 1024; // 16MB
    const allowedTypes = ['application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'];
    
    if (file) {
        if (file.size > maxSize) {
            showNotification('Le fichier est trop volumineux. Taille maximum : 16MB', 'error');
            input.value = '';
            return false;
        }
        
        if (!allowedTypes.includes(file.type)) {
            showNotification('Format de fichier non supporté. Utilisez PDF, DOC ou DOCX', 'error');
            input.value = '';
            return false;
        }
    }
    
    return true;
}

// Validation des dates de rendez-vous
function validateAppointmentDate(input) {
    const selectedDate = new Date(input.value);
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    
    if (selectedDate < today) {
        showNotification('Veuillez sélectionner une date future', 'error');
        input.value = '';
        return false;
    }
    
    return true;
}

// Smooth scroll pour les ancres
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Animation du navbar au scroll
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    }
});

// Lazy loading des images
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// Amélioration de l'accessibilité
document.addEventListener('keydown', function(e) {
    // Fermer le chat avec Escape
    if (e.key === 'Escape') {
        const chatContainer = document.getElementById('chat-container');
        if (chatContainer && chatContainer.style.display === 'flex') {
            chatContainer.style.display = 'none';
        }
    }
});

// Performance : Debounce pour les événements de scroll
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Appliquer le debounce aux événements de scroll
const debouncedScrollHandler = debounce(function() {
    // Code de gestion du scroll optimisé
}, 16);

window.addEventListener('scroll', debouncedScrollHandler); 