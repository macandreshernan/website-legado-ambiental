
/**
 * Internationalization (i18n) Script
 * Handles loading translations and updating the UI.
 * Embedded translations to support file:// protocol without CORS errors.
 */

const defaultLang = 'es-MX';
const supportedLangs = ['es-MX', 'en-US'];

const translations = {
    'es-MX': {
        "nav": {
            "about": "Quiénes Somos",
            "services": "Servicios",
            "portfolio": "Portafolio",
            "experience": "Experiencia",
            "contact": "Contacto",
            "faq": "FAQ",
            "quote": "Cotizar",
            "home": "Inicio"
        },
        "hero": {
            "title": "Construyendo Infraestructura, Sosteniendo el Futuro.",
            "subtitle": "Excelencia profesional en construcción civil y legado ambiental para proyectos privados y gubernamentales en todo el mundo.",
            "portfolio_btn": "Ver Portafolio",
            "contact_btn": "Contáctanos"
        },
        "stats": {
            "years": "Años de Experiencia",
            "projects": "Proyectos Completados",
            "certifications": "Certificaciones ISO"
        },
        "value": {
            "title": "Excelencia en Construcción Civil y Legado Ambiental",
            "desc": "Entregamos soluciones de ingeniería de alto impacto con un compromiso inquebrantable con la calidad, la seguridad y el desarrollo sostenible. Nuestro legado se construye sobre la fortaleza de nuestras estructuras y la salud de nuestro medio ambiente.",
            "mission_btn": "Conoce Más Sobre Nuestra Misión"
        },
        "services": {
            "label": "Lo que hacemos",
            "title": "Nuestros Servicios Especializados",
            "desc": "Ofrecemos consultoría integral en ingeniería y medio ambiente para diversos sectores.",
            "civil": {
                "title": "Ingeniería Civil",
                "desc": "Diseño estructural y obras civiles pesadas para infraestructura industrial y pública."
            },
            "env": {
                "title": "Legado Ambiental",
                "desc": "Prácticas de construcción sostenible y mitigación del impacto ambiental."
            },
            "mgmt": {
                "title": "Gestión de Proyectos",
                "desc": "Gestión integral asegurando cronogramas, presupuesto y estándares de seguridad."
            },
            "gov": {
                "title": "Proyectos Gubernamentales",
                "desc": "Soluciones especializadas para licitaciones de obras públicas municipales y federales."
            },
            "details": "Detalles"
        },
        "portfolio": {
            "title": "Proyectos Recientes",
            "p1": {
                "cat": "Gobierno / Infraestructura",
                "title": "Sistema de Viaducto Metropolitano",
                "desc": "Proyecto de conexión urbana de 1.5km."
            },
            "p2": {
                "cat": "Privado / Comercial",
                "title": "Centro Empresarial Solaris",
                "desc": "Sede comercial con certificación ecológica."
            }
        },
        "cta": {
            "title": "¿Listo para Construir tu Legado?",
            "desc": "Contacta a nuestro equipo de ingeniería hoy para una consulta integral sobre tu próximo proyecto privado o gubernamental.",
            "start_btn": "Iniciar un Proyecto",
            "download_btn": "Descargar Portafolio"
        },
        "footer": {
            "desc": "Definiendo la excelencia en el entorno construido mientras preservamos el legado natural de nuestro planeta.",
            "services": {
                "title": "Servicios",
                "1": "Ingeniería Civil",
                "2": "Impacto Ambiental",
                "3": "Diseño de Infraestructura",
                "4": "Desarrollo Urbano"
            },
            "company": {
                "title": "Compañía",
                "1": "Sobre Nuestra Firma",
                "2": "Portafolio de Proyectos",
                "3": "Certificaciones",
                "4": "Oportunidades Laborales"
            },
            "contact": {
                "title": "Contacto",
                "addr_1": "Engineering Plaza, Suite 400",
                "addr_2": "International Business District"
            },
            "rights": "© 2024 Legado Ambiental. Todos los derechos reservados.",
            "privacy": "Política de Privacidad",
            "terms": "Términos de Servicio",
            "sitemap": "Mapa del Sitio"
        },
        "about": {
            "title": "Quiénes Somos",
            "hero": {
                "title": "Quiénes Somos",
                "subtitle": "Definiendo el paisaje de la ingeniería civil a través de la integridad, precisión y un compromiso con la infraestructura sostenible."
            },
            "sustainable": {
                "title": "Construyendo un Legado Sostenible",
                "p1": "Fundada en 2010, Legado Ambiental se ha establecido como una piedra angular de la excelencia en ingeniería tanto en el sector público como en el privado. Nos especializamos en proyectos de infraestructura complejos que exigen alta competencia técnica y sensibilidad ambiental.",
                "p2": "Nuestro enfoque combina la maestría en ingeniería tradicional con tecnologías sostenibles modernas, asegurando que cada proyecto que emprendemos sirva a la comunidad para las generaciones venideras."
            },
            "mission": {
                "title": "Misión",
                "desc": "Proveer soluciones de ingeniería civil de vanguardia que integren la sostenibilidad ambiental con la eficiencia técnica, superando las expectativas de nuestros clientes en el sector público y privado mediante un compromiso inquebrantable con la calidad y la seguridad."
            },
            "vision": {
                "title": "Visión",
                "desc": "Consolidarnos como la firma líder en infraestructura civil y ambiental en la región, siendo reconocidos por nuestra capacidad de innovación, resiliencia técnica y por dejar un legado positivo en cada comunidad donde desarrollamos nuestros proyectos."
            },
            "values": {
                "title": "Nuestros Valores",
                "subtitle": "Los Pilares de Nuestro Éxito",
                "integrity": "Integridad",
                "integrity_desc": "Actuamos con transparencia absoluta en cada licitación y ejecución de obra, garantizando la confianza de nuestros socios gubernamentales y privados.",
                "sustainability": "Sostenibilidad",
                "sustainability_desc": "Diseñamos pensando en el mañana. Priorizamos materiales y procesos que minimicen el impacto ambiental y maximicen la vida útil de la infraestructura.",
                "excellence": "Excelencia",
                "excellence_desc": "Desde la planeación hasta el último detalle de acabado, buscamos la perfección técnica y funcional en todos nuestros desafíos de ingeniería."
            },
            "cta": {
                "title": "Construyamos el futuro juntos",
                "desc": "Contacte a nuestro equipo de expertos para discutir cómo Legado Ambiental puede hacer realidad su próxima visión con precisión y cuidado.",
                "btn_consult": "Iniciar Consulta",
                "btn_portfolio": "Ver Portafolio"
            }
        },
        "services_page": {
            "title": "Nuestros Servicios Especializados de Ingeniería y Construcción",
            "hero_desc": "Ofrecemos soluciones de infraestructura y construcción sostenible adaptadas tanto para la iniciativa privada como para iniciativas gubernamentales en la región.",
            "tabs": {
                "all": "Todos los Servicios",
                "private": "Sector Privado",
                "public": "Obras Públicas"
            },
            "private": {
                "title": "Construcción Privada",
                "desc": "Ingeniería integral para complejos residenciales de alta gama, sedes corporativas y naves industriales estratégicas. Nos centramos en la excelencia estructural y la eficiencia ambiental.",
                "list": {
                    "1": "Desarrollos Residenciales",
                    "2": "Centros Comerciales y Corporativos",
                    "3": "Centros Logísticos e Industriales"
                },
                "btn": "Conocer Más"
            },
            "public": {
                "title": "Obras Civiles Gubernamentales",
                "desc": "Proyectos de infraestructura pública a gran escala, incluyendo desarrollo urbano, sistemas de carreteras e instalaciones públicas esenciales. Cumplimos con los más altos estándares de seguridad y normativa.",
                "list": {
                    "1": "Infraestructura Urbana y Vialidades",
                    "2": "Escuelas y Hospitales Públicos",
                    "3": "Saneamiento Ambiental"
                },
                "btn": "Ver Proyectos"
            },
            "extra": {
                "title": "Capacidades Adicionales",
                "design": "Diseño de Proyectos",
                "design_desc": "Desde el concepto hasta los planos.",
                "maintenance": "Mantenimiento",
                "maintenance_desc": "Cuidado posterior a la construcción.",
                "consulting": "Consultoría Ecológica",
                "consulting_desc": "Certificación de edificios verdes.",
                "audit": "Auditoría de Calidad",
                "audit_desc": "Informes de integridad estructural."
            },
            "cta": {
                "title": "¿Listo para comenzar tu próximo proyecto?",
                "desc": "Legado Ambiental aporta décadas de experiencia colectiva a cada obra. Hablemos de tus requerimientos hoy mismo.",
                "btn_quote": "Obtener Cotización",
                "btn_process": "Nuestro Proceso"
            }
        },
        "portfolio_page": {
            "title": "Portafolio de Proyectos | Legado Ambiental",
            "hero": {
                "title": "Nuestro Legado en Infraestructura",
                "desc": "Explora una selección de nuestros proyectos más impactantes que definen paisajes urbanos y conectan comunidades."
            },
            "tabs": {
                "all": "Todos los Proyectos",
                "commercial": "Comercial",
                "infrastructure": "Infraestructura",
                "eco": "Ecológicos"
            },
            "items": {
                "p1": {
                    "cat": "Ecológico / Oficina",
                    "title": "Torre Vértice Verde",
                    "desc": "Un edificio de uso mixto de 45 pisos con certificación LEED Platino, integrando jardines verticales y sistemas de recolección de agua pluvial."
                },
                "p2": {
                    "cat": "Infraestructura",
                    "title": "Puente del Río Azul"
                },
                "p3": {
                    "cat": "Público / Transporte",
                    "title": "Expansión Terminal 3"
                },
                "p4": {
                    "cat": "Cultural",
                    "title": "Museo de Arte Moderno del Norte",
                    "desc": "Un hito cultural con una fachada geométrica única."
                },
                "p5": {
                    "cat": "Energía",
                    "title": "Parque Solar Helios"
                }
            },
            "load_more": "Cargar Más Proyectos",
            "cta": {
                "title": "¿Listo para ser parte de nuestro próximo capítulo?",
                "desc": "Nos asociamos con visionarios que buscan construir algo duradero. Comencemos a planificar tu proyecto.",
                "btn": "Contactar Ahora"
            }
        },
        "experience_page": {
            "title": "Nuestra Experiencia | Legado Ambiental",
            "hero": {
                "title": "Un Legado de Excelencia en Ingeniería",
                "desc": "Explora los hitos que han definido nuestro crecimiento e impacto en la industria de la construcción durante la última década."
            },
            "timeline": {
                "2024": {
                    "title": "Expansión Global",
                    "desc": "Legado Ambiental abrió su primera sede internacional, marcando un nuevo capítulo en nuestra misión de brindar soluciones sostenibles a escala global."
                },
                "2020": {
                    "title": "La Iniciativa Sostenible",
                    "desc": "Lanzamos nuestro departamento de Consultoría Ecológica, integrando materiales verdes y prácticas de eficiencia energética en todos nuestros proyectos de construcción."
                },
                "2015": {
                    "title": "Primer Contrato Gubernamental",
                    "desc": "Adjudicación de nuestro primer gran proyecto de infraestructura pública: la revitalización del sistema de carreteras del centro de la ciudad."
                },
                "2010": {
                    "title": "Fundación",
                    "desc": "Legado Ambiental fue fundada por un equipo de cuatro ingenieros civiles apasionados por combinar la integridad estructural con la administración ambiental."
                }
            }
        },
        "contact_page": {
            "title": "Contacto y FAQ | Legado Ambiental",
            "hero": {
                "title": "Ponte en Contacto",
                "desc": "Estamos aquí para ayudar con cualquier pregunta sobre nuestros servicios o proyectos. Completa el formulario a continuación o explora nuestras preguntas frecuentes."
            },
            "form": {
                "title": "Envíanos un Mensaje",
                "name": "Nombre",
                "name_ph": "Tu Nombre Completo",
                "email": "Correo Electrónico",
                "subject": "Asunto",
                "options": {
                    "general": "Consulta General",
                    "quote": "Solicitud de Presupuesto",
                    "proposal": "Propuesta de Proyecto",
                    "jobs": "Oportunidades de Empleo"
                },
                "message": "Mensaje",
                "message_ph": "¿Cómo podemos ayudarte?",
                "btn": "Enviar Mensaje"
            },
            "faq": {
                "title": "Preguntas Frecuentes",
                "q1": "¿Qué tipos de certificación ambiental manejan?",
                "a1": "Trabajamos con estándares LEED, BREEAM y normativas locales de impacto ambiental. Nuestro equipo puede guiar todo el proceso de certificación para su proyecto.",
                "q2": "¿Realizan proyectos fuera de la región?",
                "a2": "Sí, nuestra división de Expansión Global gestiona proyectos internacionales. Contáctenos para discutir la logística y viabilidad de su ubicación.",
                "q3": "¿Ofrecen servicios de solo diseño?",
                "a3": "Absolutamente. Ofrecemos servicios modulares que van desde el diseño conceptual y planos estructurales hasta la gestión completa de la construcción llave en mano."
            },
            "info": {
                "title": "Información Directa",
                "addr": "Plaza de Ingeniería, Suite 400<br />Distrito de Negocios Internacional"
            }
        },
        "index_landing": {
            "title": "Legado Ambiental",
            "welcome": "Bienvenido al proyecto de preservación ambiental."
        }
    },
    'en-US': {
        "nav": {
            "about": "About Us",
            "services": "Services",
            "portfolio": "Portfolio",
            "experience": "Experience",
            "contact": "Contact",
            "faq": "FAQ",
            "quote": "Get a Quote",
            "home": "Home"
        },
        "hero": {
            "title": "Building Infrastructure, Sustaining the Future.",
            "subtitle": "Professional excellence in civil construction and environmental legacy for private and government projects worldwide.",
            "portfolio_btn": "View Portfolio",
            "contact_btn": "Contact Us"
        },
        "stats": {
            "years": "Years of Experience",
            "projects": "Completed Projects",
            "certifications": "ISO Certifications"
        },
        "value": {
            "title": "Excellence in Civil Construction and Environmental Legacy",
            "desc": "We deliver high-impact engineering solutions with unwavering commitment to quality, safety, and sustainable development. Our legacy is built on the strength of our structures and the health of our environment.",
            "mission_btn": "Learn More About Our Mission"
        },
        "services": {
            "label": "What We Do",
            "title": "Our Specialized Services",
            "desc": "We offer comprehensive options in engineering and environment for various sectors.",
            "civil": {
                "title": "Civil Engineering",
                "desc": "Structural design and heavy civil works for industrial and public infrastructure."
            },
            "env": {
                "title": "Environmental Legacy",
                "desc": "Sustainable construction practices and environmental impact mitigation."
            },
            "mgmt": {
                "title": "Project Management",
                "desc": "Integral management ensuring schedules, budgets, and safety standards."
            },
            "gov": {
                "title": "Government Projects",
                "desc": "Specialized solutions for municipal and federal public works tenders."
            },
            "details": "Details"
        },
        "portfolio": {
            "title": "Recent Projects",
            "p1": {
                "cat": "Government / Infrastructure",
                "title": "Metropolitan Viaduct System",
                "desc": "1.5km urban connection project."
            },
            "p2": {
                "cat": "Private / Commercial",
                "title": "Solaris Business Center",
                "desc": "Commercial headquarters with ecological certification."
            }
        },
        "cta": {
            "title": "Ready to Build Your Legacy?",
            "desc": "Contact our engineering team today for a comprehensive consultation on your next private or government project.",
            "start_btn": "Start a Project",
            "download_btn": "Download Portfolio"
        },
        "footer": {
            "desc": "Defining excellence in the built environment while preserving our planet's natural legacy.",
            "services": {
                "title": "Services",
                "1": "Civil Engineering",
                "2": "Environmental Impact",
                "3": "Infrastructure Design",
                "4": "Urban Development"
            },
            "company": {
                "title": "Company",
                "1": "About Our Firm",
                "2": "Project Portfolio",
                "3": "Certifications",
                "4": "Career Opportunities"
            },
            "contact": {
                "title": "Contact",
                "addr_1": "Engineering Plaza, Suite 400",
                "addr_2": "International Business District"
            },
            "rights": "© 2024 Legado Ambiental. All rights reserved.",
            "privacy": "Privacy Policy",
            "terms": "Terms of Service",
            "sitemap": "Sitemap"
        },
        "about": {
            "title": "About Us",
            "hero": {
                "title": "About Us",
                "subtitle": "Defining the landscape of civil engineering through integrity, precision, and a commitment to sustainable infrastructure."
            },
            "sustainable": {
                "title": "Building a Sustainable Legacy",
                "p1": "Founded in 2010, Legado Ambiental has established itself as a cornerstone of engineering excellence in both the public and private sectors. We specialize in complex infrastructure projects that demand high technical competence and environmental sensitivity.",
                "p2": "Our approach combines traditional engineering mastery with modern sustainable technologies, ensuring that every project we undertake serves the community for generations to come."
            },
            "mission": {
                "title": "Mission",
                "desc": "To provide state-of-the-art civil engineering solutions that integrate environmental sustainability with technical efficiency, exceeding our clients' expectations in the public and private sectors through an unwavering commitment to quality and safety."
            },
            "vision": {
                "title": "Vision",
                "desc": "To consolidate ourselves as the leading civil and environmental infrastructure firm in the region, recognized for our innovation capacity, technical resilience, and for leaving a positive legacy in every community where we develop our projects."
            },
            "values": {
                "title": "Our Values",
                "subtitle": "The Pillars of Our Success",
                "integrity": "Integrity",
                "integrity_desc": "We act with absolute transparency in every tender and work execution, guaranteeing the trust of our government and private partners.",
                "sustainability": "Sustainability",
                "sustainability_desc": "We design thinking about tomorrow. We prioritize materials and processes that minimize environmental impact and maximize infrastructure lifespan.",
                "excellence": "Excellence",
                "excellence_desc": "From planning to the last finishing detail, we seek technical and functional perfection in all our engineering challenges."
            },
            "cta": {
                "title": "Let's Build the Future Together",
                "desc": "Contact our team of experts to discuss how Legado Ambiental can make your next vision a reality with precision and care.",
                "btn_consult": "Start Consultation",
                "btn_portfolio": "View Portfolio"
            }
        },
        "services_page": {
            "title": "Our Specialized Engineering and Construction Services",
            "hero_desc": "We offer infrastructure and sustainable construction solutions adapted for both private initiative and government initiatives in the region.",
            "tabs": {
                "all": "All Services",
                "private": "Private Sector",
                "public": "Public Works"
            },
            "private": {
                "title": "Private Construction",
                "desc": "Integral engineering for high-end residential complexes, corporate headquarters, and strategic industrial warehouses. We focus on structural excellence and environmental efficiency.",
                "list": {
                    "1": "Residential Developments",
                    "2": "Commercial and Corporate Centers",
                    "3": "Logistics and Industrial Centers"
                },
                "btn": "Learn More"
            },
            "public": {
                "title": "Government Civil Works",
                "desc": "Large-scale public infrastructure projects, including urban development, road systems, and essential public facilities. We comply with the highest safety and regulatory standards.",
                "list": {
                    "1": "Urban Infrastructure and Roadways",
                    "2": "Public Schools and Hospitals",
                    "3": "Environmental Sanitation"
                },
                "btn": "View Projects"
            },
            "extra": {
                "title": "Additional Capabilities",
                "design": "Project Design",
                "design_desc": "From concept to blueprints.",
                "maintenance": "Maintenance",
                "maintenance_desc": "Post-construction care.",
                "consulting": "Ecological Consulting",
                "consulting_desc": "Green building certification.",
                "audit": "Quality Audit",
                "audit_desc": "Structural integrity reports."
            },
            "cta": {
                "title": "Ready to Start Your Next Project?",
                "desc": "Legado Ambiental brings decades of collective experience to every job. Let's talk about your requirements today.",
                "btn_quote": "Get a Quote",
                "btn_process": "Our Process"
            }
        },
        "portfolio_page": {
            "title": "Project Portfolio | Legado Ambiental",
            "hero": {
                "title": "Our Legacy in Infrastructure",
                "desc": "Explore a selection of our most impactful projects that define urban landscapes and connect communities."
            },
            "tabs": {
                "all": "All Projects",
                "commercial": "Commercial",
                "infrastructure": "Infrastructure",
                "eco": "Eco-friendly"
            },
            "items": {
                "p1": {
                    "cat": "Eco-friendly / Office",
                    "title": "Green Vertex Tower",
                    "desc": "A 45-story mixed-use building with LEED Platinum certification, integrating vertical gardens and rainwater harvesting systems."
                },
                "p2": {
                    "cat": "Infrastructure",
                    "title": "Blue River Bridge"
                },
                "p3": {
                    "cat": "Public / Transport",
                    "title": "Terminal 3 Expansion"
                },
                "p4": {
                    "cat": "Cultural",
                    "title": "Northern Modern Art Museum",
                    "desc": "A cultural landmark with a unique geometric facade."
                },
                "p5": {
                    "cat": "Energy",
                    "title": "Helios Solar Park"
                }
            },
            "load_more": "Load More Projects",
            "cta": {
                "title": "Ready to Be Part of Our Next Chapter?",
                "desc": "We partner with visionaries seeking to build something lasting. Let's start planning your project.",
                "btn": "Contact Now"
            }
        },
        "experience_page": {
            "title": "Our Experience | Legado Ambiental",
            "hero": {
                "title": "A Legacy of Engineering Excellence",
                "desc": "Explore the milestones that have defined our growth and impact in the construction industry over the last decade."
            },
            "timeline": {
                "2024": {
                    "title": "Global Expansion",
                    "desc": "Legado Ambiental opened its first international headquarters, marking a new chapter in our mission to provide sustainable solutions on a global scale."
                },
                "2020": {
                    "title": "The Sustainable Initiative",
                    "desc": "We launched our Ecological Consulting department, integrating green materials and energy efficiency practices into all our construction projects."
                },
                "2015": {
                    "title": "First Government Contract",
                    "desc": "Award of our first major public infrastructure project: the revitalization of the downtown highway system."
                },
                "2010": {
                    "title": "Foundation",
                    "desc": "Legado Ambiental was founded by a team of four civil engineers passionate about combining structural integrity with environmental stewardship."
                }
            }
        },
        "contact_page": {
            "title": "Contact & FAQ | Legado Ambiental",
            "hero": {
                "title": "Get in Touch",
                "desc": "We are here to help with any questions about our services or projects. Fill out the form below or explore our frequently asked questions."
            },
            "form": {
                "title": "Send Us a Message",
                "name": "Name",
                "name_ph": "Your Full Name",
                "email": "Email",
                "subject": "Subject",
                "options": {
                    "general": "General Inquiry",
                    "quote": "Quote Request",
                    "proposal": "Project Proposal",
                    "jobs": "Job Opportunities"
                },
                "message": "Message",
                "message_ph": "How can we help you?",
                "btn": "Send Message"
            },
            "faq": {
                "title": "Frequently Asked Questions",
                "q1": "What types of environmental certification do you handle?",
                "a1": "We work with LEED, BREEAM, and local environmental impact regulations. Our team can guide the entire certification process for your project.",
                "q2": "Do you do projects outside the region?",
                "a2": "Yes, our Global Expansion division manages international projects. Contact us to discuss the logistics and viability of your location.",
                "q3": "Do you offer design-only services?",
                "a3": "Absolutely. We offer modular services ranging from conceptual design and structural blueprints to complete turnkey construction management."
            },
            "info": {
                "title": "Direct Information",
                "addr": "Engineering Plaza, Suite 400<br />International Business District"
            }
        },
        "index_landing": {
            "title": "Legado Ambiental",
            "welcome": "Welcome to the environmental preservation project."
        }
    }
};

/**
 * Gets the initial language preference.
 * Priority: LocalStorage > Browser Language > Default
 */
function getInitialLanguage() {
    // Check for query param first (SEO friendly)
    const urlParams = new URLSearchParams(window.location.search);
    const paramLang = urlParams.get('lang');
    if (paramLang && supportedLangs.includes(paramLang)) {
        return paramLang;
    }

    const savedLang = localStorage.getItem('site-lang');
    if (savedLang && supportedLangs.includes(savedLang)) {
        return savedLang;
    }

    const browserLang = navigator.language;
    // Map browser language to supported variants if needed
    if (browserLang.startsWith('es')) return 'es-MX';
    if (browserLang.startsWith('en')) return 'en-US';

    return defaultLang;
}

/**
 * Loads translations for the specified language.
 * Now simply returns from the embedded object.
 * @param {string} lang 
 */
async function loadTranslations(lang) {
    if (translations[lang]) {
        return translations[lang];
    }
    console.error(`Translations not found for ${lang}`);
    return null;
}

/**
 * Helper to get nested value from dot notation string
 * @param {object} obj 
 * @param {string} path 
 */
function getValueByPath(obj, path) {
    return path.split('.').reduce((acc, part) => acc && acc[part], obj);
}

/**
 * Applies translations to the DOM.
 * @param {object} translationsData 
 */
function applyTranslations(translationsData) {
    if (!translationsData) return;

    const elements = document.querySelectorAll('[data-i18n]');
    elements.forEach(element => {
        const key = element.getAttribute('data-i18n');
        // Because keys in JSON are nested (e.g. "nav.about"), we need to resolve them
        // In the original JSON structure, they were nested.
        // Let's implement a resolver.
        const text = getValueByPath(translationsData, key);

        if (text) {
            // Handle different element types if necessary (e.g., inputs)
            if (element.tagName === 'INPUT' && element.getAttribute('placeholder')) {
                // Actually for placeholders we usually use data-i18n-placeholder
                // But let's check if the element has data-i18n-placeholder attribute
            }
            element.innerHTML = text; // Use innerHTML to support <br>
        }
    });

    // Handle placeholders
    const placeholders = document.querySelectorAll('[data-i18n-placeholder]');
    placeholders.forEach(element => {
        const key = element.getAttribute('data-i18n-placeholder');
        const text = getValueByPath(translationsData, key);
        if (text) {
            element.setAttribute('placeholder', text);
        }
    });

    // Handle specific dropdown options if they are not covered by data-i18n on the option tag directly?
    // The HTML has data-i18n on option tags, so getValueByPath should work for them too.

    // Dispatch event to notify that language has changed
    document.dispatchEvent(new CustomEvent('languageChanged', { detail: { translations: translationsData } }));
}

/**
 * Sets the current language.
 * @param {string} lang 
 */
async function setLanguage(lang) {
    if (!supportedLangs.includes(lang)) {
        console.warn(`Language ${lang} not supported.`);
        return;
    }

    const translationsData = await loadTranslations(lang);
    if (translationsData) {
        applyTranslations(translationsData);
        localStorage.setItem('site-lang', lang);
        document.documentElement.lang = lang.split('-')[0]; // Update html lang attribute
        updateActiveLanguageUI(lang);
    }
}

/**
 * Updates the UI active state for language selectors.
 */
function updateActiveLanguageUI(lang) {
    // Update style of active button
    document.querySelectorAll('[data-switch-lang]').forEach(btn => {
        if (btn.getAttribute('data-switch-lang') === lang) {
            btn.classList.add('text-primary'); // Active style from Tailwind
            btn.classList.remove('text-gray-500'); // Assuming inactive style
        } else {
            btn.classList.remove('text-primary');
            btn.classList.add('text-gray-500'); // Assuming inactive style if we had one
        }
    });
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    const currentLang = getInitialLanguage();
    setLanguage(currentLang);

    // Bind click events to language switchers if they exist
    // Expected structure: <button ... data-switch-lang="en-US">EN</button>
    document.body.addEventListener('click', (e) => {
        const switcher = e.target.closest('[data-switch-lang]');
        if (switcher) {
            e.preventDefault();
            const lang = switcher.getAttribute('data-switch-lang');
            setLanguage(lang);
        }
    });
});
