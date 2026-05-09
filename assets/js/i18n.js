
/**
 * Internationalization (i18n) Script
 * Handles loading translations and updating the UI.
 * Embedded translations to support file:// protocol without CORS errors.
 */

const defaultLang = 'es-MX';
const supportedLangs = ['es-MX', 'en-US'];

const translations = {
    "es-MX": {
        "nav": {
            "about": "Quiénes Somos",
            "services": "Servicios y Cotización",
            "portfolio": "Portafolio",
            "experience": "Experiencia",
            "contact": "Contacto",
            "faq": "FAQ",
            "quote": "Cotizar",
            "home": "Inicio",
            "theme": "Cambiar Tema"
        },
        "hero": {
            "title": "Protegiendo hoy, el legado del mañana.",
            "subtitle": "Ingeniería para una productividad amigable con el medio ambiente.",
            "portfolio_btn": "Ver Portafolio",
            "contact_btn": "Contáctanos"
        },
        "stats": {
            "years": "Años de Experiencia",
            "projects": "Proyectos Completados",
            "certifications": "Certificaciones ISO"
        },
        "value": {
            "title": "Soluciones Inteligentes y Proyectos Integrales para el Desarrollo Sostenible.",
            "desc": "Excelencia en Construcción Civil y Legado Ambiental.",
            "mission_btn": "Conoce Más Sobre Nuestra Misión"
        },
        "services": {
            "label": "Lo que hacemos",
            "title": "Nuestros Servicios Especializados",
            "desc": "Ofrecemos consultoría integral en ingeniería y medio ambiente para diversos sectores.",
            "s1": {
                "title": "Ingeniería Ambiental",
                "desc": "Somos una firma de ingeniería especializada en medio ambiente, integrada por un equipo interdisciplinario de profesionales con amplia experiencia en estudios, proyectos, construcción y consultoría ambiental."
            },
            "s2": {
                "title": "Construcción",
                "desc": "Infraestructura, desarrollo urbano, vivienda, obra pública y privada, así como consultorías técnicas especializadas, participando en todas las etapas del proyecto: planeación, ejecución, supervisión y cierre técnico–administrativo."
            },
            "s3": {
                "title": "Topografía",
                "desc": "Brindamos servicios topográficos de alta precisión para proyectos de infraestructura, obra civil, urbanización, transporte y edificación, apoyados en tecnología moderna y metodologías estandarizadas."
            },
            "s4": {
                "title": "Seguridad e Higiene",
                "desc": "En Legado Ambiental, transformamos la operatividad de sus proyectos integrando seguridad, eficiencia administrativa y cumplimiento legal. Bajo la Dirección de Operaciones y Cumplimiento Integral, ofrecemos soluciones robustas para los sectores de la construcción y el medio ambiente."
            },
            "details": "Detalles"
        },
        "portfolio": {
            "label": "Nuestro Trabajo",
            "title": "Proyectos Recientes",
            "p1": {
                "cat": "Grupo Serla",
                "title": "Estudio de impacto ambiental",
                "desc": "Estudio integral corporativo bajo la NOM-052-SEMARNAT (Residuos Peligrosos), NOM-085 (Emisiones) y disposiciones del RCDF, asegurando operaciones sin externalidades negativas."
            },
            "p2": {
                "cat": "Río Tiloxtoc",
                "title": "Saneamiento",
                "desc": "Planeación, muestreo y mitigación conjunta con CIITEC-IPN, alineados a la Ley Federal de Aguas y normativas SEMARNAT para el rescate de ecosistemas."
            }
        },
        "cta": {
            "title": "¿Listo para Construir tu Legado?",
            "desc": "Contacta a nuestro equipo de ingeniería hoy para una consulta integral sobre tu próximo proyecto privado o gubernamental.",
            "start_btn": "Iniciar un Proyecto",
            "download_btn": "Descargar Portafolio"
        },
        "footer": {
            "title": "Legado Ambiental <br>S.A. de C.V.",
            "desc": "Soluciones holísticas para el desarrollo de infraestructura y cumplimiento normativo.",
            "services": {
                "1": "Ingeniería Ambiental",
                "2": "Construcción",
                "3": "Topografía",
                "4": "Seguridad e Higiene",
                "title": "Servicios"
            },
            "company": {
                "1": "Quiénes somos",
                "2": "Servicios",
                "3": "Experiencia",
                "4": "Contacto",
                "title": "Compañía"
            },
            "contact": {
                "title": "Contacto",
                "addr_1": "U.H. Valle de Ecatepec, C.P. 55119",
                "addr_2": "Ecatepec, Estado de México",
                "phone_1": "55 7312 6918",
                "phone_2": "72 2672 7212",
                "email": "<strong>legado.ambiental.mx@gmail.com</strong>"
            },
            "rights": "<strong>© {{year}} Legado Ambiental S.A. de C.V. <br>Todos los derechos reservados.</strong>",
            "privacy": "Política de Privacidad",
            "terms": "Términos de Servicio",
            "sitemap": "Mapa del Sitio"
        },
        "about": {
            "title": "Quiénes Somos",
            "hero": {
                "title": "Quiénes Somos",
                "subtitle": "Somos una firma de ingeniería especializada en medio ambiente, integrada por un equipo interdisciplinario"
            },
            "sustainable": {
                "title": "Construyendo un Legado Sostenible",
                "p1": "Legado Ambiental, S.A. de C.V. es una empresa mexicana fundada en 1999 con sede en la Ciudad de México, especializada en prestación de servicios profesionales en los ámbitos de la ingeniería ambiental, construcción, topografía y seguridad e higiene en obra, como una respuesta a la creciente necesidad de lograr una alta compatibilidad entre las actividades productivas, la prevención, control de la contaminación ambiental y la preservación de los recursos naturales, orientado al desarrollo sostenible.",
                "p2": "Somos una firma de ingeniería especializada en medio ambiente, integrada por un equipo interdisciplinario de profesionales con amplia experiencia en estudios, proyectos, construcción y consultoría ambiental. Por más de dos décadas hemos colaborado con los sectores industrial, gubernamental y de servicios en el diseño y aplicación de soluciones de ingeniería ambiental técnica, económica y ambientalmente factibles."
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
            },
            "objective": {
                "title": "Nuestro Objetivo",
                "desc": "\"Ser la firma líder en México que revoluciona la ingeniería civil y ambiental, creando proyectos estratégicos que protegen la vida, el entorno y el futuro de las ciudades.\""
            }
        },
        "services_page": {
            "title": "Nuestros Servicios Especializados de Ingeniería y Construcción",
            "hero_desc": "Ofrecemos soluciones de infraestructura y construcción sostenible adaptadas tanto para la iniciativa privada como para iniciativas gubernamentales en la región.",
            "tabs": {
                "engeneering": "Ingeniería Ambiental",
                "building": "Construcción",
                "topography": "Topografía",
                "safety": "Seguridad e Higiene",
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
            },
            "methodology": {
                "subtitle": "Proceso Ejecutivo",
                "title": "Nuestra Metodología Estratégica"
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
                "item1": {
                    "label": "Industria",
                    "title": "Evaluación Ambiental - <strong>Grupo Serla</strong>",
                    "desc": "Estudio integral corporativo bajo la <strong>NOM-052-SEMARNAT</strong> (RPs), <strong>NOM-085</strong> (Emisiones) y las disposiciones del <strong>RCDF</strong>, asegurando operatividad sin externalidades negativas."
                },
                "item2": {
                    "label": "Hídrico",
                    "title": "Saneamiento - Río Tiloxtoc",
                    "desc": "Planeación, muestreo y mitigación conjunta con el <strong>CIITEC-IPN</strong> acorde a los lineamientos de la <strong>Ley de Aguas Nacionales</strong> y <strong>SEMARNAT</strong> para el rescate ecológico."
                },
                "item3": {
                    "label": "Academia",
                    "title": "Tecnología Sustentable - <strong>ITESM</strong>",
                    "desc": "Implementación de redes hidrosanitarias cerradas y Plantas de Tratamiento Paquete cumpliendo con las <strong>Normas Técnicas</strong> del <strong>Reglamento de Construcciones</strong> y el <strong>Tecnológico de Monterrey</strong>."
                },
                "item4": {
                    "label": "Especialidad",
                    "title": "Tratamiento Alta Eficiencia - <strong>IMMSA</strong>",
                    "desc": "Diseño estructural avanzado bajo requerimientos sísmicos y la <strong>NOM-001-SEMARNAT-1996</strong> para la máxima remoción fisicoquímica de metales pesados en el sector metalúrgico."
                },
                "item5": {
                    "label": "Salud",
                    "title": "Unidades Clínicas y Hospitales",
                    "desc": "Adecuación estructural catalogada como <strong>Grupo A</strong> (U=1.5) integrando alta bioseguridad bajo la <strong>NOM-087-ECOL-SSA1</strong> en materia de <strong>Residuos Peligrosos Biológico Infecciosos</strong>."
                },
                "item6": {
                    "label": "<strong>1999</strong>",
                    "title": "Fundación y Obras Civiles",
                    "desc": "Consolidación operacional operando en conjunto con el <strong>Título Sexto del RCDF</strong>, logrando una firme planeación empresarial equilibrada entre construcción y medio ambiente."
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
                "email_ph": "nombre@ejemplo.com",
                "subject": "Asunto",
                "options": {
                    "general": "Consulta General",
                    "quote": "Solicitud de Presupuesto",
                    "proposal": "Propuesta de Proyecto",
                    "jobs": "Oportunidades de Empleo"
                },
                "lastname": "Apellidos",
                "lastname_ph": "Tus Apellidos",
                "phone": "Teléfono",
                "phone_ph": "(55) 1234 5678",
                "method_label": "Medio de Contacto Preferido",
                "method_email": "Correo Electrónico",
                "method_phone": "Llamada Telefónica",
                "honeypot": "Si eres humano, deja este campo en blanco",
                "captcha_label": "Resuelve:",
                "captcha_error": "Resultado incorrecto",
                "phone_error": "Formato inválido. (55) 1234 5678",
                "email_error": "Correo inválido",
                "message": "Mensaje",
                "message_ph": "¿Cómo podemos ayudarte?",
                "btn": "Enviar Mensaje",
                "sending": "Enviando mensaje..."
            },
            "faq": {
                "title": "Preguntas Frecuentes",
                "q1": "¿Qué beneficios obtengo al contratar su servicio de supervisión en obra pública o privada?",
                "a1": "Garantizamos la optimización de costos operativos, la reducción de riesgos legales y el cumplimiento estricto de los estándares técnicos y regulatorios vigentes.",
                "q2": "¿Realizan proyectos de vivienda?",
                "a2": "Sí, aplicamos servicios de topografía y control de obra específicamente para el diseño y construcción de vivienda y desarrollos urbanos.",
                "q3": "¿Sus soluciones ambientales son técnica y económicamente viables?",
                "a3": "Sí, nuestro enfoque de más de dos décadas se centra en diseñar soluciones que sean factibles tanto técnica como económica y ambientalmente, orientadas siempre al desarrollo sostenible.",
                "q4": "¿Sus cursos de capacitación tienen validez oficial?",
                "a4": "Sí, todos nuestros cursos son impartidos por un Agente Capacitador Externo (ACE) debidamente registrado ante la STPS.",
                "q5": "¿Qué documentos entregan al finalizar una capacitación en SST?",
                "a5": "Entregamos las constancias de habilidades laborales (DC-3) y el soporte documental necesario para acreditar el cumplimiento normativo ante las autoridades.",
                "q6": "¿Pueden ayudarnos a crear un departamento de Seguridad y Salud en el Trabajo desde cero?",
                "a6": "Sí, somos especialistas en la instauración de departamentos de Seguridad y Salud en el Trabajo (SST), encargándonos del diseño y la coordinación integral."
            },
            "info": {
                "title": "Información Directa",
                "addr": "U.H. Valle de Ecatepec, <br> C.P. 55119, Ecatepec, Estado de México",
                "email": "<strong>legado.ambiental.mx@gmail.com</strong>",
                "phone1": "+52 55 7312 6918",
                "phone2": "+52 72 2672 7212"
            }
        },
        "index_landing": {
            "title": "Legado Ambiental",
            "title_full": "Legado Ambiental | Inicio",
            "welcome": "Bienvenido al proyecto de preservación ambiental."
        },
        "error_404": {
            "title": "404 - Página no encontrada",
            "desc": "Lo sentimos, la página que buscas no existe o ha sido movida. Estamos construyendo nuevos componentes para mejorar su experiencia.",
            "btn": "Volver al Inicio"
        },
        "auto_generated": {
            "auto_generated.text_001": "Legado\n                        Ambiental",
            "auto_generated.text_002": "<span class=\"w-8 h-[2px] bg-primary/50\"></span>\n<span data-i18n=\"services.label\">Lo que hacemos</span>",
            "auto_generated.text_003": "<a class=\"hover:text-primary transition-colors\" data-i18n=\"footer.services.1\" href=\"services_overview/services.html#tab-1\">Ingeniería Ambiental</a>",
            "auto_generated.text_004": "<a class=\"hover:text-primary transition-colors\" data-i18n=\"footer.services.2\" href=\"services_overview/services.html#tab-2\">Construcción</a>",
            "auto_generated.text_005": "<a class=\"hover:text-primary transition-colors\" data-i18n=\"footer.services.3\" href=\"services_overview/services.html#tab-3\">Topografía</a>",
            "auto_generated.text_006": "<a class=\"hover:text-primary transition-colors\" data-i18n=\"footer.services.4\" href=\"services_overview/services.html#tab-4\">Seguridad e Higiene</a>",
            "auto_generated.text_007": "<a class=\"hover:text-primary transition-colors\" data-i18n=\"footer.company.1\" href=\"about_us/about_us.html\">Quiénes somos</a>",
            "auto_generated.text_008": "<a class=\"hover:text-primary transition-colors\" data-i18n=\"footer.company.2\" href=\"services_overview/services.html\">Servicios</a>",
            "auto_generated.text_009": "<a class=\"hover:text-primary transition-colors\" data-i18n=\"footer.company.3\" href=\"experience_timeline/our_experience.html\">Experiencia</a>",
            "auto_generated.text_010": "<a class=\"hover:text-primary transition-colors\" data-i18n=\"footer.company.4\" href=\"faq/contact_faq.html\">Contacto</a>",
            "auto_generated.text_011": "<span class=\"material-symbols-outlined text-sm text-primary\">location_on</span>\n<span data-i18n=\"footer.contact.addr_1\">U.H. Valle de Ecatepec, C.P. 55119</span>\n<span data-i18n=\"footer.contact.addr_2\">Ecatepec, Estado de México</span>",
            "auto_generated.text_012": "<span class=\"material-symbols-outlined text-sm text-primary\">call</span>\n<span data-i18n=\"footer.contact.phone_1\">55 7312 6918</span>",
            "auto_generated.text_013": "<span class=\"material-symbols-outlined text-sm text-primary\">call</span>\n<span data-i18n=\"footer.contact.phone_2\">72 2672 7212</span>",
            "auto_generated.text_014": "<span class=\"material-symbols-outlined text-sm text-primary\">mail</span>\n<span data-i18n=\"footer.contact.email\"><strong>legado.ambiental.mx@gmail.com</strong></span>",
            "auto_generated.text_015": "<span class=\"material-symbols-outlined text-[1.2rem]\">dark_mode</span>",
            "auto_generated.text_016": "<span class=\"material-symbols-outlined text-3xl\">menu</span>",
            "auto_generated.text_017": "<span class=\"material-symbols-outlined text-lg\">dark_mode</span>\n<span class=\"text-base font-semibold\" data-i18n=\"nav.theme\">Cambiar Tema</span>",
            "auto_generated.text_018": "<span data-i18n=\"hero.portfolio_btn\">Ver Portafolio</span>\n<span class=\"material-symbols-outlined\">trending_flat</span>",
            "auto_generated.text_019": "<span data-i18n=\"value.mission_btn\">Conoce Más Sobre Nuestra Misión</span>\n<span class=\"material-symbols-outlined\">download</span>",
            "auto_generated.text_020": "<span data-i18n=\"services.details\">Detalles</span>\n<span class=\"material-symbols-outlined ml-2 transform group-hover:translate-x-2 transition-transform\">\n                                arrow_forward\n                            </span>",
            "auto_generated.text_021": "<span data-i18n=\"services.details\">Detalles</span>\n<span class=\"material-symbols-outlined ml-2 transform group-hover:translate-x-2 transition-transform\">\n                                arrow_forward\n                            </span>",
            "auto_generated.text_022": "<span data-i18n=\"services.details\">Detalles</span>\n<span class=\"material-symbols-outlined ml-2 transform group-hover:translate-x-2 transition-transform\">\n                                arrow_forward\n                            </span>",
            "auto_generated.text_023": "<span data-i18n=\"services.details\">Detalles</span>\n<span class=\"material-symbols-outlined ml-2 transform group-hover:translate-x-2 transition-transform\">\n                                arrow_forward\n                            </span>",
            "auto_generated.text_024": "<span class=\"material-symbols-outlined transform group-hover:translate-x-1 transition-transform\">arrow_forward</span>",
            "auto_generated.text_025": "<span class=\"material-symbols-outlined transform group-hover:translate-x-1 transition-transform\">arrow_forward</span>",
            "auto_generated.text_026": "Amamos la vida y nuestro trabajo, por ello, la seguridad de las personas, así como la protección y la restauración del entorno son nuestra máxima prioridad. Cada proyecto de ingeniería que firmamos tiene el propósito consciente de elevar la calidad de vida y proteger todas las formas de existencia.",
            "auto_generated.text_027": "Somos agentes de cambio. Fomentamos una cultura de desarrollo sostenible en nuestros colaboradores, proveedores y clientes. No solo entregamos soluciones técnicas; impulsamos una transformación profunda en los procesos industriales y urbanos para heredar un planeta sano.",
            "auto_generated.text_028": "Luchamos incansablemente por la mejora continua. Nos preparamos técnica y humanamente cada día para que nuestra \"Alta Ingeniería\" no solo satisfaga, sino que supere las expectativas de nuestros clientes, persistiendo con disciplina hasta alcanzar la excelencia en cada obra.",
            "auto_generated.text_029": "<span class=\"w-8 h-[2px] bg-emerald-500/50\"></span>\n              Nuestros Valores\n              <span class=\"w-8 h-[2px] bg-emerald-500/50\"></span>",
            "auto_generated.text_030": "Los Pilares de Nuestra <br/>\n<span class=\"text-transparent bg-clip-text bg-gradient-to-r from-emerald-500 to-cyan-500\">Transformación Ambiental</span>",
            "auto_generated.text_031": "Filosofía Ecológica y<br/><span class=\"text-emerald-500 font-bold\">Respeto a la Vida</span>",
            "auto_generated.text_032": "Conciencia Ambiental<br/><span class=\"text-cyan-500 font-bold\">Trascendente</span>",
            "auto_generated.text_033": "Excelencia, Disciplina y<br/><span class=\"text-blue-500 font-bold\">Persistencia Evolutiva</span>",
            "auto_generated.text_034": "Legado\n              Ambiental",
            "auto_generated.text_035": "Transformación Ambiental",
            "auto_generated.text_036": "Respeto a la Vida",
            "auto_generated.text_037": "Trascendente",
            "auto_generated.text_038": "Persistencia Evolutiva",
            "auto_generated.text_039": "<a class=\"inline-flex items-center text-sm font-medium text-gray-300 hover:text-white transition-colors\" href=\"../home.html\">\n<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Inicio</span>\n</a>",
            "auto_generated.text_040": "<span class=\"material-symbols-outlined text-[1.2rem]\">dark_mode</span>",
            "auto_generated.text_041": "<span class=\"material-symbols-outlined text-3xl\">menu</span>",
            "auto_generated.text_042": "<span class=\"material-symbols-outlined text-lg\">dark_mode</span>\n<span class=\"text-base font-semibold\" data-i18n=\"nav.theme\">Cambiar Tema</span>",
            "auto_generated.text_043": "<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Inicio</span>",
            "auto_generated.text_044": "<span class=\"material-symbols-outlined\">share</span>",
            "auto_generated.text_045": "<span class=\"material-symbols-outlined\">mail</span>",
            "auto_generated.text_046": "Esta categoría agrupa el análisis técnico y la planeación operativa para todo tipo de\n                                desechos.",
            "auto_generated.text_047": "Enfocada en la infraestructura y el aprovechamiento eficiente del recurso hídrico.",
            "auto_generated.text_048": "Servicios clave para asegurar que las empresas cumplan con la normativa ambiental\n                                vigente.",
            "auto_generated.text_049": "Servicios educativos para empresas o entidades gubernamentales.",
            "auto_generated.text_050": "Desarrollamos espacios habitables con altos estándares de diseño y funcionalidad.",
            "auto_generated.text_051": "Especialistas en obras técnicas para el manejo y saneamiento del agua.",
            "auto_generated.text_052": "La base técnica que asegura la viabilidad de cualquier construcción.",
            "auto_generated.text_053": "Aseguramos que su inversión se ejecute conforme a lo planeado.",
            "auto_generated.text_054": "Protegemos el activo más valioso de su organización: su capital humano, garantizando el\n                                cumplimiento total ante la STPS y autoridades locales.",
            "auto_generated.text_055": "Supervisión en Proyectos de Alto Riesgo: Vigilancia presencial y control de protocolos\n                                de seguridad en obras civiles, proyectos ambientales e industriales.",
            "auto_generated.text_056": "Capacitación Certificada (STPS): Cursos y talleres impartidos por un Agente Capacitador\n                                Externo (ACE) con registro oficial ante la Secretaría del Trabajo. Busca nuestro catalogo de capacitación en: <strong><a href='https://agentes.stps.gob.mx/Buscador/BuscadorAgente.aspx'>https://agentes.stps.gob.mx/Buscador/BuscadorAgente.aspx</a></strong><br/> Usando nuestro registro como <strong>HELI8812234B1</strong> (RFC).",
            "auto_generated.text_057": "Gestión Integral de Residuos (Sólidos y Peligrosos)",
            "auto_generated.text_058": "Ingeniería Hídrica y Soluciones de Agua",
            "auto_generated.text_059": "Consultoría, Dictámenes y Cumplimiento Legal",
            "auto_generated.text_060": "Fortalecimiento de Capacidades",
            "auto_generated.text_061": "Edificación Residencial y Vivienda",
            "auto_generated.text_062": "Infraestructura Hidráulica y Ambiental",
            "auto_generated.text_063": "Ingeniería de Proyecto y Planeación",
            "auto_generated.text_064": "Supervisión y Control de Obra",
            "auto_generated.text_065": "Levantamientos y Estudios Topográficos",
            "auto_generated.text_066": "Georreferenciación y Precisión GPS",
            "auto_generated.text_067": "Modelado Digital y Visualización",
            "auto_generated.text_068": "Control y Supervisión de Obra",
            "auto_generated.text_069": "Estructura y Gestión Operativa (Consultoría)",
            "auto_generated.text_070": "Supervisión Técnica y Seguridad en Campo",
            "auto_generated.text_071": "Formación Especializada y Capacitación (ACE)",
            "auto_generated.text_072": "Legado\n                            Ambiental",
            "auto_generated.text_073": "<strong>Diagnóstico y Caracterización: </strong> Estudios de caracterización\n                                        de residuos sólidos, diagnósticos y muestreo.",
            "auto_generated.text_074": "<strong>Planes de Manejo:</strong> Elaboración de planes de manejo integral\n                                        para residuos sólidos\n                                        y peligrosos, incluyendo clasificación y seguimiento.",
            "auto_generated.text_075": "<strong>Logística y Recolección:</strong>Estudio y\n                                        optimización de rutas y métodos de recolección.",
            "auto_generated.text_076": "<strong>Infraestructura:</strong>Proyectos para rellenos sanitarios,\n                                        tratamiento de residuos orgánicos y obras para el manejo de residuos peligrosos.",
            "auto_generated.text_077": "Realizar cotización",
            "auto_generated.text_078": "<strong>Tratamiento de Aguas:</strong> Diseño, construcción y supervisión de\n                                        plantas de tratamiento de aguas residuales.",
            "auto_generated.text_079": "<strong>Sustentabilidad Hídrica:</strong> Sistemas alternativos de reciclaje o\n                                        reutilización, programas de ahorro de agua y estudios técnicos de ahorro.",
            "auto_generated.text_080": "<strong>Análisis Especializado:</strong> Estudios hidrometeorológicos para\n                                        planeación y prevención.",
            "auto_generated.text_081": "Realizar cotización",
            "auto_generated.text_082": "<strong>Evaluaciones de Impacto:</strong> Estudios de impacto ambiental\n                                        (EsIA), diagnósticos y evaluaciones ambientales preventivas.",
            "auto_generated.text_083": "<strong>Documentación Oficial:</strong> Elaboración de informes técnicos y\n                                        dictámenes ambientales con validez legal.",
            "auto_generated.text_084": "Realizar cotización",
            "auto_generated.text_085": "<strong>Capacitación:</strong> Cursos, talleres y programas de formación en\n                                        temas ambientales.",
            "auto_generated.text_086": "Realizar cotización",
            "auto_generated.text_087": "<strong>Vivienda Unifamiliar:</strong> Construcción de casas personalizadas y\n                                        residencias de alto nivel.",
            "auto_generated.text_088": "<strong>Vivienda Multifamiliar:</strong> Desarrollo de complejos de\n                                        departamentos, edificios residenciales y desarrollos habitacionales.",
            "auto_generated.text_089": "<strong>Proyectos Llave en Mano: </strong> Gestión total desde la cimentación\n                                        hasta los acabados finales.",
            "auto_generated.text_090": "Realizar cotización",
            "auto_generated.text_091": "<strong>Plantas de Tratamiento de Aguas Residuales (PTAR):</strong> Diseño,\n                                        construcción y puesta en marcha de sistemas de tratamiento industrial y\n                                        municipal.",
            "auto_generated.text_092": "<strong>Obras de Saneamiento:</strong> Infraestructura para la reutilización\n                                        de agua y sistemas de drenaje especializado.",
            "auto_generated.text_093": "Realizar cotización",
            "auto_generated.text_094": "<strong>Elaboración de Proyectos Ejecutivos:</strong> Diseño arquitectónico,\n                                        cálculos estructurales, instalaciones hidrosanitarias y eléctricas.",
            "auto_generated.text_095": "<strong>Gestión de Trámites y Licencias:</strong> Apoyo técnico para la\n                                        obtención de permisos de construcción y autorizaciones ambientales.",
            "auto_generated.text_096": "Realizar cotización",
            "auto_generated.text_097": "<strong>Supervisión Técnica de Obra:</strong> Vigilancia presencial para\n                                        garantizar el cumplimiento de planos, especificaciones y calidad de\n                                        materiales.",
            "auto_generated.text_098": "<strong>Control de Costos y Tiempos:</strong> Administración de cronogramas\n                                        de obra (Ruta Crítica) y presupuestos para evitar desviaciones.",
            "auto_generated.text_099": "<strong>Auditoría de Obra:</strong> Verificación de procesos constructivos y\n                                        normativas de seguridad en sitio.",
            "auto_generated.text_100": "Realizar cotización",
            "auto_generated.text_101": "<strong>Definición</strong> exacta de contornos espaciales y dimensiones del\n                                        terreno para cimientos seguros.",
            "auto_generated.text_102": "Realizar cotización",
            "auto_generated.text_103": "<strong>Ubicación</strong> de coordenadas geoespaciales precisas usando\n                                        tecnología global de vanguardia.",
            "auto_generated.text_104": "Realizar cotización",
            "auto_generated.text_105": "<strong>Generación</strong> de entornos de terreno tridimensionales (3D) para\n                                        cálculos volumétricos exactos.",
            "auto_generated.text_106": "Realizar cotización",
            "auto_generated.text_107": "<strong>Verificación</strong> constante de trazos en terreno real para\n                                        garantizar el alineamiento con planimetría.",
            "auto_generated.text_108": "Realizar cotización",
            "auto_generated.text_109": "<strong>Instauración de Departamentos de SST:</strong> Diseño, implementación\n                                        y coordinación integral de departamentos de Seguridad e Higiene\n                                        Industrial.",
            "auto_generated.text_110": "<strong>Auditorías de Cumplimiento Normativo:</strong> Diagnóstico y\n                                        aseguramiento de las Normas Oficiales Mexicanas (NOM) vigentes (Seguridad, Salud\n                                        y Organización).",
            "auto_generated.text_111": "<strong>Gestión de Comisiones Mixtas:</strong> Constitución y capacitación de\n                                        la Comisión de Seguridad e Higiene (NOM-019-STPS).",
            "auto_generated.text_112": "<strong>Elaboración de Programas Específicos:</strong> Manuales de seguridad,\n                                        programas de protección civil y planes de respuesta a emergencias.",
            "auto_generated.text_113": "Realizar cotización",
            "auto_generated.text_114": "<strong>Análisis de Riesgos por Puesto de Trabajo\n                                            (AST):</strong>Identificación de peligros y evaluación de riesgos para\n                                        prevenir accidentes y enfermedades laborales.",
            "auto_generated.text_115": "<strong>Verificación de Equipos y Maquinaria:</strong> Inspección de\n                                        condiciones de seguridad en herramientas, andamios y maquinaria pesada.",
            "auto_generated.text_116": "Realizar cotización",
            "auto_generated.text_117": "<strong>Emisión de Constancias DC-3:</strong>Entrega de documentos de\n                                        habilidades laborales con validez ante inspecciones federales.",
            "auto_generated.text_118": "<strong>Entrenamiento en Trabajos de Alto Riesgo:</strong> Capacitación\n                                        específica en alturas, espacios confinados, corte y soldadura, y manejo de\n                                        sustancias químicas.",
            "auto_generated.text_119": "<strong>Formación de Brigadas de Emergencia:</strong> CPrimeros auxilios,\n                                        prevención y combate de incendios, y evacuación de inmuebles.",
            "auto_generated.text_120": "Realizar cotización",
            "auto_generated.text_121": "<a class=\"inline-flex items-center text-sm font-medium text-gray-300 hover:text-white transition-colors\" href=\"../home.html\">\n<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Inicio</span>\n</a>",
            "auto_generated.text_122": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Diagnóstico y Caracterización: </strong> Estudios de caracterización\n                                        de residuos sólidos, diagnósticos y muestreo.\n                                    </span>",
            "auto_generated.text_123": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Planes de Manejo:</strong> Elaboración de planes de manejo integral\n                                        para residuos sólidos\n                                        y peligrosos, incluyendo clasificación y seguimiento.</span>",
            "auto_generated.text_124": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Logística y Recolección:</strong>Estudio y\n                                        optimización de rutas y métodos de recolección.\n                                    </span>",
            "auto_generated.text_125": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Infraestructura:</strong>Proyectos para rellenos sanitarios,\n                                        tratamiento de residuos orgánicos y obras para el manejo de residuos peligrosos.\n                                    </span>",
            "auto_generated.text_126": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Tratamiento de Aguas:</strong> Diseño, construcción y supervisión de\n                                        plantas de tratamiento de aguas residuales.</span>",
            "auto_generated.text_127": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Sustentabilidad Hídrica:</strong> Sistemas alternativos de reciclaje o\n                                        reutilización, programas de ahorro de agua y estudios técnicos de ahorro.</span>",
            "auto_generated.text_128": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Análisis Especializado:</strong> Estudios hidrometeorológicos para\n                                        planeación y prevención.</span>",
            "auto_generated.text_129": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Evaluaciones de Impacto:</strong> Estudios de impacto ambiental\n                                        (EsIA), diagnósticos y evaluaciones ambientales preventivas.</span>",
            "auto_generated.text_130": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Documentación Oficial:</strong> Elaboración de informes técnicos y\n                                        dictámenes ambientales con validez legal.</span>",
            "auto_generated.text_131": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Capacitación:</strong> Cursos, talleres y programas de formación en\n                                        temas ambientales.</span>",
            "auto_generated.text_132": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Vivienda Unifamiliar:</strong> Construcción de casas personalizadas y\n                                        residencias de alto nivel.</span>",
            "auto_generated.text_133": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Vivienda Multifamiliar:</strong> Desarrollo de complejos de\n                                        departamentos, edificios residenciales y desarrollos habitacionales.</span>",
            "auto_generated.text_134": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Proyectos Llave en Mano: </strong> Gestión total desde la cimentación\n                                        hasta los acabados finales.</span>",
            "auto_generated.text_135": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Plantas de Tratamiento de Aguas Residuales (PTAR):</strong> Diseño,\n                                        construcción y puesta en marcha de sistemas de tratamiento industrial y\n                                        municipal.</span>",
            "auto_generated.text_136": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Obras de Saneamiento:</strong> Infraestructura para la reutilización\n                                        de agua y sistemas de drenaje especializado.</span>",
            "auto_generated.text_137": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Elaboración de Proyectos Ejecutivos:</strong> Diseño arquitectónico,\n                                        cálculos estructurales, instalaciones hidrosanitarias y eléctricas.</span>",
            "auto_generated.text_138": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Gestión de Trámites y Licencias:</strong> Apoyo técnico para la\n                                        obtención de permisos de construcción y autorizaciones ambientales.</span>",
            "auto_generated.text_139": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Supervisión Técnica de Obra:</strong> Vigilancia presencial para\n                                        garantizar el cumplimiento de planos, especificaciones y calidad de\n                                        materiales.</span>",
            "auto_generated.text_140": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Control de Costos y Tiempos:</strong> AAdministración de cronogramas\n                                        de obra (Ruta Crítica) y presupuestos para evitar desviaciones.</span>",
            "auto_generated.text_141": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Auditoría de Obra:</strong> Verificación de procesos constructivos y\n                                        normativas de seguridad en sitio.</span>",
            "auto_generated.text_142": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Definición</strong> exacta de contornos espaciales y dimensiones del\n                                        terreno para cimientos seguros.</span>",
            "auto_generated.text_143": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Ubicación</strong> de coordenadas geoespaciales precisas usando\n                                        tecnología global de vanguardia.</span>",
            "auto_generated.text_144": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Generación</strong> de entornos de terreno tridimensionales (3D) para\n                                        cálculos volumétricos exactos.</span>",
            "auto_generated.text_145": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Verificación</strong> constante de trazos en terreno real para\n                                        garantizar el alineamiento con planimetría.</span>",
            "auto_generated.text_146": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Instauración de Departamentos de SST:</strong> Diseño, implementación\n                                        y coordinación integral de departamentos de Seguridad e Higiene\n                                        Industrial.</span>",
            "auto_generated.text_147": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Auditorías de Cumplimiento Normativo:</strong> Diagnóstico y\n                                        aseguramiento de las Normas Oficiales Mexicanas (NOM) vigentes (Seguridad, Salud\n                                        y Organización).</span>",
            "auto_generated.text_148": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Gestión de Comisiones Mixtas:</strong> Constitución y capacitación de\n                                        la Comisión de Seguridad e Higiene (NOM-019-STPS).</span>",
            "auto_generated.text_149": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Elaboración de Programas Específicos:</strong> Manuales de seguridad,\n                                        programas de protección civil y planes de respuesta a emergencias.</span>",
            "auto_generated.text_150": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Análisis de Riesgos por Puesto de Trabajo\n                                            (AST):</strong>Identificación de peligros y evaluación de riesgos para\n                                        prevenir accidentes y enfermedades laborales.</span>",
            "auto_generated.text_151": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Verificación de Equipos y Maquinaria:</strong> Inspección de\n                                        condiciones de seguridad en herramientas, andamios y maquinaria pesada.</span>",
            "auto_generated.text_152": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Emisión de Constancias DC-3:</strong>Entrega de documentos de\n                                        habilidades laborales con validez ante inspecciones federales.</span>",
            "auto_generated.text_153": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Entrenamiento en Trabajos de Alto Riesgo:</strong> Capacitación\n                                        específica en alturas, espacios confinados, corte y soldadura, y manejo de\n                                        sustancias químicas.</span>",
            "auto_generated.text_154": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Formación de Brigadas de Emergencia:</strong> CPrimeros auxilios,\n                                        prevención y combate de incendios, y evacuación de inmuebles.</span>",
            "auto_generated.text_155": "<span class=\"material-symbols-outlined text-[1.2rem]\">dark_mode</span>",
            "auto_generated.text_156": "<span class=\"material-symbols-outlined text-3xl\">menu</span>",
            "auto_generated.text_157": "<span class=\"material-symbols-outlined text-lg\">dark_mode</span>\n<span class=\"text-base font-semibold\" data-i18n=\"nav.theme\">Cambiar Tema</span>",
            "auto_generated.text_158": "<span>Realizar cotización</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_159": "<span>Realizar cotización</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_160": "<span>Realizar cotización</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_161": "<span>Realizar cotización</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_162": "<span>Realizar cotización</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_163": "<span>Realizar cotización</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_164": "<span>Realizar cotización</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_165": "<span>Realizar cotización</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_166": "<span>Realizar cotización</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_167": "<span>Realizar cotización</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_168": "<span>Realizar cotización</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_169": "<span>Realizar cotización</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_170": "<span>Realizar cotización</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_171": "<span>Realizar cotización</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_172": "<span>Realizar cotización</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_173": "<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Inicio</span>",
            "auto_generated.text_174": "<span class=\"material-symbols-outlined\">share</span>",
            "auto_generated.text_175": "<span class=\"material-symbols-outlined\">mail</span>",
            "auto_generated.text_176": "Legado\n                            Ambiental",
            "auto_generated.text_177": "<a class=\"inline-flex items-center text-sm font-medium text-gray-700 hover:text-primary dark:text-gray-400 dark:hover:text-white\" href=\"../home.html\">\n<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Inicio</span>\n</a>",
            "auto_generated.text_178": "<span class=\"material-symbols-outlined text-[1.2rem]\">dark_mode</span>",
            "auto_generated.text_179": "<span class=\"material-symbols-outlined text-3xl\">menu</span>",
            "auto_generated.text_180": "<span class=\"material-symbols-outlined text-lg\">dark_mode</span>\n<span class=\"text-base font-semibold\" data-i18n=\"nav.theme\">Cambiar Tema</span>",
            "auto_generated.text_181": "<span data-i18n=\"portfolio_page.load_more\">Cargar Más Proyectos</span> <span class=\"material-symbols-outlined text-[18px]\">expand_more</span>",
            "auto_generated.text_182": "<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Inicio</span>",
            "auto_generated.text_183": "<span class=\"material-symbols-outlined\">share</span>",
            "auto_generated.text_184": "<span class=\"material-symbols-outlined\">mail</span>",
            "auto_generated.text_185": "<span data-i18n=\"experience_page.timeline.item1.title\">Evaluación Ambiental - <strong>Grupo Serla</strong></span>",
            "auto_generated.text_186": "<span data-i18n=\"experience_page.timeline.item2.title\">Saneamiento - Río Tiloxtoc</span>",
            "auto_generated.text_187": "<span data-i18n=\"experience_page.timeline.item3.title\">Tecnología Sustentable - <strong>ITESM</strong></span>",
            "auto_generated.text_188": "<span data-i18n=\"experience_page.timeline.item4.title\">Tratamiento Alta Eficiencia - <strong>IMMSA</strong></span>",
            "auto_generated.text_189": "<span data-i18n=\"experience_page.timeline.item5.title\">Unidades Clínicas y Hospitales</span>",
            "auto_generated.text_190": "<span data-i18n=\"experience_page.timeline.item6.title\">Fundación y Obras Civiles</span>",
            "auto_generated.text_191": "Legado\n              Ambiental",
            "auto_generated.text_192": "<a class=\"inline-flex items-center text-sm font-medium text-gray-300 hover:text-white transition-colors\" href=\"../home.html\">\n<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Inicio</span>\n</a>",
            "auto_generated.text_193": "<span class=\"material-symbols-outlined text-[1.2rem]\">dark_mode</span>",
            "auto_generated.text_194": "<span class=\"material-symbols-outlined text-3xl\">menu</span>",
            "auto_generated.text_195": "<span class=\"material-symbols-outlined text-lg\">dark_mode</span>\n<span class=\"text-base font-semibold\" data-i18n=\"nav.theme\">Cambiar Tema</span>",
            "auto_generated.text_196": "<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Inicio</span>",
            "auto_generated.text_197": "<span class=\"material-symbols-outlined\">share</span>",
            "auto_generated.text_198": "<span class=\"material-symbols-outlined\">mail</span>",
            "auto_generated.text_199": "Legado\n                            Ambiental",
            "auto_generated.text_200": "<a class=\"inline-flex items-center text-sm font-medium text-gray-300 hover:text-white transition-colors\" href=\"../home.html\">\n<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Inicio</span>\n</a>",
            "auto_generated.text_201": "<span class=\"material-symbols-outlined text-primary w-10 h-10 bg-primary/10 rounded-xl flex items-center justify-center w-full sm:w-auto justify-center\">call</span>\n<span data-i18n=\"contact_page.info.phone1\">+52 55 7312 6918</span>",
            "auto_generated.text_202": "<span class=\"material-symbols-outlined text-primary w-10 h-10 bg-primary/10 rounded-xl flex items-center justify-center w-full sm:w-auto justify-center\">call</span>\n<span data-i18n=\"contact_page.info.phone2\">+52 72 2672 7212</span>",
            "auto_generated.text_203": "<span class=\"material-symbols-outlined text-primary w-10 h-10 bg-primary/10 rounded-xl flex items-center justify-center w-full sm:w-auto justify-center\">mail</span>\n<span data-i18n=\"contact_page.info.email\"><strong>legado.ambiental.mx@gmail.com</strong></span>",
            "auto_generated.text_204": "<span class=\"material-symbols-outlined text-primary w-10 h-10 bg-primary/10 rounded-xl flex items-center justify-center w-full sm:w-auto justify-center\">location_on</span>\n<span data-i18n=\"contact_page.info.addr\">U.H. Valle de Ecatepec, <br/> C.P. 55119, Ecatepec, Estado de México</span>",
            "auto_generated.text_205": "<span class=\"material-symbols-outlined text-[1.2rem]\">dark_mode</span>",
            "auto_generated.text_206": "<span class=\"material-symbols-outlined text-3xl\">menu</span>",
            "auto_generated.text_207": "<span class=\"material-symbols-outlined text-lg\">dark_mode</span>\n<span class=\"text-base font-semibold\" data-i18n=\"nav.theme\">Cambiar Tema</span>",
            "auto_generated.text_208": "<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Inicio</span>",
            "auto_generated.text_209": "<span class=\"material-symbols-outlined\">share</span>",
            "auto_generated.text_210": "<span class=\"material-symbols-outlined\">mail</span>",
            "auto_generated.text_211": "© 2024 Legado Ambiental. <span data-i18n=\"footer.rights\"><strong>© {{year}} Legado Ambiental S.A. de C.V. <br/>Todos los derechos reservados.</strong></span>",
            "auto_generated.text_212": "<span class=\"material-symbols-outlined text-xl\">dark_mode</span>",
            "auto_generated.text_213": "<span class=\"material-symbols-outlined\">home</span>\n<span data-i18n=\"error_404.btn\">Volver al Inicio</span>"
        }
    },
    "en-US": {
        "nav": {
            "about": "About Us",
            "services": "Services & Quote",
            "portfolio": "Portfolio",
            "experience": "Experience",
            "contact": "Contact",
            "faq": "FAQ",
            "quote": "Get a Quote",
            "home": "Home",
            "theme": "Toggle Theme"
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
            "s1": {
                "title": "Environmental Engineering",
                "desc": "We are an engineering firm specialized in the environment, integrated by an interdisciplinary team of professionals with extensive experience in environmental studies, projects, construction, and consulting."
            },
            "s2": {
                "title": "Construction",
                "desc": "Infrastructure, urban development, housing, public and private works, as well as specialized technical consulting, participating in all stages of the project: planning, execution, supervision, and technical-administrative closure."
            },
            "s3": {
                "title": "Topography",
                "desc": "We provide high-precision topographic services for infrastructure, civil works, urbanization, transport, and building projects, supported by modern technology and standardized methodologies."
            },
            "s4": {
                "title": "Health & Safety",
                "desc": "At Legado Ambiental, we transform the operability of your projects by integrating safety, administrative efficiency, and legal compliance. Under the Direction of Operations and Comprehensive Compliance, we offer robust solutions for the construction and environmental sectors."
            },
            "details": "Details"
        },
        "portfolio": {
            "label": "Our Work",
            "title": "Recent Projects",
            "p1": {
                "cat": "Grupo Serla",
                "title": "Environmental Impact Study",
                "desc": "Comprehensive corporate study under NOM-052-SEMARNAT (Hazardous Waste), NOM-085 (Emissions), and RCDF provisions, ensuring operations without negative externalities."
            },
            "p2": {
                "cat": "Tiloxtoc River",
                "title": "Sanitation",
                "desc": "Planning, sampling, and joint mitigation with CIITEC-IPN, aligned with the National Water Law and SEMARNAT regulations for ecosystem rescue."
            }
        },
        "cta": {
            "title": "Ready to Build Your Legacy?",
            "desc": "Contact our engineering team today for a comprehensive consultation on your next private or government project.",
            "start_btn": "Start a Project",
            "download_btn": "Download Portfolio"
        },
        "footer": {
            "title": "Legado Ambiental <br>S.A. de C.V.",
            "desc": "Holistic solutions for infrastructure development and regulatory compliance.",
            "services": {
                "1": "Environmental Engineering",
                "2": "Construction",
                "3": "Topography",
                "4": "Health & Safety",
                "title": "Services"
            },
            "company": {
                "1": "About Us",
                "2": "Services",
                "3": "Experience",
                "4": "Contact",
                "title": "Company"
            },
            "contact": {
                "title": "Contact",
                "addr_1": "U.H. Valle de Ecatepec, C.P. 55119",
                "addr_2": "Ecatepec, State of Mexico",
                "phone_1": "55 7312 6918",
                "phone_2": "72 2672 7212",
                "email": "<strong>legado.ambiental.mx@gmail.com</strong>"
            },
            "rights": "<strong>© {{year}} Legado Ambiental S.A. de C.V. <br>All rights reserved.</strong>",
            "privacy": "Privacy Policy",
            "terms": "Terms of Service",
            "sitemap": "Sitemap"
        },
        "about": {
            "title": "About Us",
            "hero": {
                "title": "About Us",
                "subtitle": "We are an environmental engineering firm, integrated by an interdisciplinary team"
            },
            "sustainable": {
                "title": "Building a Sustainable Legacy",
                "p1": "Legado Ambiental, S.A. de C.V. is a Mexican company founded in 1999 based in Mexico City, specialized in providing professional services in the fields of environmental engineering, construction, topography, and health & safety in construction, as a response to the growing need to achieve high compatibility between productive activities, prevention, environmental pollution control, and natural resource preservation, oriented towards sustainable development.",
                "p2": "We are an engineering firm specialized in the environment, integrated by an interdisciplinary team of professionals with extensive experience in environmental studies, projects, construction, and consulting. For over two decades we have collaborated with the industrial, government, and service sectors in the design and application of technically, economically, and environmentally feasible environmental engineering solutions."
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
            },
            "objective": {
                "title": "Our Objective",
                "desc": "\"To be the leading firm in Mexico revolutionizing civil and environmental engineering, creating strategic projects that protect life, the environment, and the future of our cities.\""
            }
        },
        "services_page": {
            "title": "Our Specialized Engineering and Construction Services",
            "hero_desc": "We offer infrastructure and sustainable construction solutions adapted for both private initiative and government initiatives in the region.",
            "tabs": {
                "all": "All Services",
                "private": "Private Sector",
                "public": "Public Works",
                "engeneering": "Environmental Engineering",
                "building": "Construction",
                "topography": "Topography",
                "safety": "Health & Safety"
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
            },
            "methodology": {
                "subtitle": "Executive Process",
                "title": "Our Strategic Methodology"
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
                "item1": {
                    "label": "Industry",
                    "title": "Environmental Assessment - <strong>Grupo Serla</strong>",
                    "desc": "Comprehensive corporate study under <strong>NOM-052-SEMARNAT</strong> (Hazardous Waste), <strong>NOM-085</strong> (Emissions), and <strong>RCDF</strong> provisions, ensuring operations with no negative externalities."
                },
                "item2": {
                    "label": "Water",
                    "title": "Sanitation - Tiloxtoc River",
                    "desc": "Planning, sampling, and joint mitigation with <strong>CIITEC-IPN</strong> according to <strong>National Water Law</strong> and <strong>SEMARNAT</strong> guidelines for ecosystem rescue."
                },
                "item3": {
                    "label": "Academia",
                    "title": "Sustainable Tech - <strong>ITESM</strong>",
                    "desc": "Implementation of closed plumbing networks and Package Treatment Plants complying with <strong>Technical Standards</strong> of <strong>Building Regulations</strong> and <strong>ITESM</strong> facilities."
                },
                "item4": {
                    "label": "Specialty",
                    "title": "High Efficiency WWTP - <strong>IMMSA</strong>",
                    "desc": "Advanced structural design under seismic requirements and <strong>NOM-001-SEMARNAT-1996</strong> for maximum physicochemical removal of heavy metals in mining."
                },
                "item5": {
                    "label": "Health",
                    "title": "Clinical & Hospital Units",
                    "desc": "Structural adaptation categorized as <strong>Group A</strong> (U=1.5) integrating maximal biosecurity under <strong>NOM-087-ECOL-SSA1</strong> regarding <strong>Hazardous Biological Infectious Wastes</strong>."
                },
                "item6": {
                    "label": "<strong>1999</strong>",
                    "title": "Foundation & Civil Works",
                    "desc": "Infrastructure consolidation operating strictly aligned with <strong>Title Six of the RCDF</strong>, achieving a balanced corporate symbiosis between construction and environment."
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
                "email_ph": "name@example.com",
                "subject": "Subject",
                "options": {
                    "general": "General Inquiry",
                    "quote": "Quote Request",
                    "proposal": "Project Proposal",
                    "jobs": "Job Opportunities"
                },
                "lastname": "Last Name",
                "lastname_ph": "Your Last Name",
                "phone": "Phone Number",
                "phone_ph": "(555) 123-4567",
                "method_label": "Preferred Contact Method",
                "method_email": "Email",
                "method_phone": "Phone Call",
                "honeypot": "If you are human, leave this field blank",
                "captcha_label": "Solve:",
                "captcha_error": "Incorrect result",
                "phone_error": "Invalid format. (555) 123-4567",
                "email_error": "Invalid email",
                "message": "Message",
                "message_ph": "How can we help you?",
                "btn": "Send Message",
                "sending": "Sending message..."
            },
            "faq": {
                "title": "Frequently Asked Questions",
                "q1": "What benefits do I get by hiring your supervision service for public or private construction?",
                "a1": "We guarantee the optimization of operational costs, the reduction of legal risks, and strict compliance with current technical and regulatory standards.",
                "q2": "Do you carry out housing projects?",
                "a2": "Yes, we apply topography and construction control services specifically for the design and construction of housing and urban developments.",
                "q3": "Are your environmental solutions technically and economically viable?",
                "a3": "Yes, our approach over more than two decades focuses on designing solutions that are technically, economically, and environmentally feasible, always oriented towards sustainable development.",
                "q4": "Are your training courses officially valid?",
                "a4": "Yes, all our courses are taught by an External Training Agent (ACE) duly registered with the STPS.",
                "q5": "What documents do you provide upon completing OHS training?",
                "a5": "We provide occupational skills certificates (DC-3) and the necessary documentary support to prove regulatory compliance before authorities.",
                "q6": "Can you help us build an Occupational Health and Safety department from scratch?",
                "a6": "Yes, we specialize in the establishment of Occupational Health and Safety (OHS) departments, handling the design and comprehensive coordination."
            },
            "info": {
                "title": "Direct Information",
                "addr": "U.H. Valle de Ecatepec, <br> C.P. 55119, Ecatepec, State of Mexico",
                "email": "<strong>legado.ambiental.mx@gmail.com</strong>",
                "phone1": "+52 55 7312 6918",
                "phone2": "+52 72 2672 7212"
            }
        },
        "index_landing": {
            "title": "Legado Ambiental",
            "title_full": "Legado Ambiental | Home",
            "welcome": "Welcome to the environmental preservation project."
        },
        "error_404": {
            "title": "404 - Page Not Found",
            "desc": "Sorry, the page you are looking for does not exist or has been moved. We are building new components to improve your experience.",
            "btn": "Back to Home"
        },
        "auto_generated": {
            "auto_generated.text_001": "Legado\n                        Ambiental",
            "auto_generated.text_002": "<span class=\"w-8 h-[2px] bg-primary/50\"></span>\n<span data-i18n=\"services.label\">What We Do</span>",
            "auto_generated.text_003": "<a class=\"hover:text-primary transition-colors\" data-i18n=\"footer.services.1\" href=\"services_overview/services.html#tab-1\">Environmental Engineering</a>",
            "auto_generated.text_004": "<a class=\"hover:text-primary transition-colors\" data-i18n=\"footer.services.2\" href=\"services_overview/services.html#tab-2\">Construction</a>",
            "auto_generated.text_005": "<a class=\"hover:text-primary transition-colors\" data-i18n=\"footer.services.3\" href=\"services_overview/services.html#tab-3\">Topography</a>",
            "auto_generated.text_006": "<a class=\"hover:text-primary transition-colors\" data-i18n=\"footer.services.4\" href=\"services_overview/services.html#tab-4\">Health & Safety</a>",
            "auto_generated.text_007": "<a class=\"hover:text-primary transition-colors\" data-i18n=\"footer.company.1\" href=\"about_us/about_us.html\">About Us</a>",
            "auto_generated.text_008": "<a class=\"hover:text-primary transition-colors\" data-i18n=\"footer.company.2\" href=\"services_overview/services.html\">Services</a>",
            "auto_generated.text_009": "<a class=\"hover:text-primary transition-colors\" data-i18n=\"footer.company.3\" href=\"experience_timeline/our_experience.html\">Experience</a>",
            "auto_generated.text_010": "<a class=\"hover:text-primary transition-colors\" data-i18n=\"footer.company.4\" href=\"faq/contact_faq.html\">Contact</a>",
            "auto_generated.text_011": "<span class=\"material-symbols-outlined text-sm text-primary\">location_on</span>\n<span data-i18n=\"footer.contact.addr_1\">U.H. Valle de Ecatepec, C.P. 55119</span>\n<span data-i18n=\"footer.contact.addr_2\">Ecatepec, State of Mexico</span>",
            "auto_generated.text_012": "<span class=\"material-symbols-outlined text-sm text-primary\">call</span>\n<span data-i18n=\"footer.contact.phone_1\">55 7312 6918</span>",
            "auto_generated.text_013": "<span class=\"material-symbols-outlined text-sm text-primary\">call</span>\n<span data-i18n=\"footer.contact.phone_2\">72 2672 7212</span>",
            "auto_generated.text_014": "<span class=\"material-symbols-outlined text-sm text-primary\">mail</span>\n<span data-i18n=\"footer.contact.email\"><strong>legado.ambiental.mx@gmail.com</strong></span>",
            "auto_generated.text_015": "<span class=\"material-symbols-outlined text-[1.2rem]\">dark_mode</span>",
            "auto_generated.text_016": "<span class=\"material-symbols-outlined text-3xl\">menu</span>",
            "auto_generated.text_017": "<span class=\"material-symbols-outlined text-lg\">dark_mode</span>\n<span class=\"text-base font-semibold\" data-i18n=\"nav.theme\">Toggle Theme</span>",
            "auto_generated.text_018": "<span data-i18n=\"hero.portfolio_btn\">View Portfolio</span>\n<span class=\"material-symbols-outlined\">trending_flat</span>",
            "auto_generated.text_019": "<span data-i18n=\"value.mission_btn\">Learn More About Our Mission</span>\n<span class=\"material-symbols-outlined\">download</span>",
            "auto_generated.text_020": "<span data-i18n=\"services.details\">Details</span>\n<span class=\"material-symbols-outlined ml-2 transform group-hover:translate-x-2 transition-transform\">\n                                arrow_forward\n                            </span>",
            "auto_generated.text_021": "<span data-i18n=\"services.details\">Details</span>\n<span class=\"material-symbols-outlined ml-2 transform group-hover:translate-x-2 transition-transform\">\n                                arrow_forward\n                            </span>",
            "auto_generated.text_022": "<span data-i18n=\"services.details\">Details</span>\n<span class=\"material-symbols-outlined ml-2 transform group-hover:translate-x-2 transition-transform\">\n                                arrow_forward\n                            </span>",
            "auto_generated.text_023": "<span data-i18n=\"services.details\">Details</span>\n<span class=\"material-symbols-outlined ml-2 transform group-hover:translate-x-2 transition-transform\">\n                                arrow_forward\n                            </span>",
            "auto_generated.text_024": "<span class=\"material-symbols-outlined transform group-hover:translate-x-1 transition-transform\">arrow_forward</span>",
            "auto_generated.text_025": "<span class=\"material-symbols-outlined transform group-hover:translate-x-1 transition-transform\">arrow_forward</span>",
            "auto_generated.text_026": "We love life and our work, therefore, the safety of people, as well as the protection and restoration of the environment are our highest priority. Every engineering project we sign has the conscious purpose of elevating the quality of life and protecting all forms of existence.",
            "auto_generated.text_027": "We are agents of change. We promote a culture of sustainable development in our collaborators, suppliers, and clients. We do not only deliver technical solutions; we drive a profound transformation in industrial and urban processes to inherit a healthy planet.",
            "auto_generated.text_028": "We strive relentlessly for continuous improvement. We prepare technically and humanely every day so that our \"High Engineering\" not only satisfies but exceeds our clients' expectations, persisting with discipline until we achieve excellence in every work.",
            "auto_generated.text_029": "<span class=\"w-8 h-[2px] bg-emerald-500/50\"></span>\n              Our Values\n              <span class=\"w-8 h-[2px] bg-emerald-500/50\"></span>",
            "auto_generated.text_030": "The Pillars of Our <br/>\n<span class=\"text-transparent bg-clip-text bg-gradient-to-r from-emerald-500 to-cyan-500\">Environmental Transformation</span>",
            "auto_generated.text_031": "Ecological Philosophy and<br/><span class=\"text-emerald-500 font-bold\">Respect for Life</span>",
            "auto_generated.text_032": "Environmental Awareness<br/><span class=\"text-cyan-500 font-bold\">Transcendent</span>",
            "auto_generated.text_033": "Excellence, Discipline and<br/><span class=\"text-blue-500 font-bold\">Evolutionary Persistence</span>",
            "auto_generated.text_034": "Legado\n              Ambiental",
            "auto_generated.text_035": "Environmental Transformation",
            "auto_generated.text_036": "Respect for Life",
            "auto_generated.text_037": "Transcendent",
            "auto_generated.text_038": "Evolutionary Persistence",
            "auto_generated.text_039": "<a class=\"inline-flex items-center text-sm font-medium text-gray-300 hover:text-white transition-colors\" href=\"../home.html\">\n<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Home</span>\n</a>",
            "auto_generated.text_040": "<span class=\"material-symbols-outlined text-[1.2rem]\">dark_mode</span>",
            "auto_generated.text_041": "<span class=\"material-symbols-outlined text-3xl\">menu</span>",
            "auto_generated.text_042": "<span class=\"material-symbols-outlined text-lg\">dark_mode</span>\n<span class=\"text-base font-semibold\" data-i18n=\"nav.theme\">Toggle Theme</span>",
            "auto_generated.text_043": "<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Home</span>",
            "auto_generated.text_044": "<span class=\"material-symbols-outlined\">share</span>",
            "auto_generated.text_045": "<span class=\"material-symbols-outlined\">mail</span>",
            "auto_generated.text_046": "This category groups the technical analysis and operational planning for all types of waste.",
            "auto_generated.text_047": "Focused on infrastructure and the efficient use of water resources.",
            "auto_generated.text_048": "Key services to ensure that companies comply with current environmental regulations.",
            "auto_generated.text_049": "Educational services for companies or government entities.",
            "auto_generated.text_050": "We develop living spaces with high standards of design and functionality.",
            "auto_generated.text_051": "Specialists in technical works for water management and sanitation.",
            "auto_generated.text_052": "The technical foundation that ensures the viability of any construction.",
            "auto_generated.text_053": "We ensure your investment is executed as planned.",
            "auto_generated.text_054": "We protect your organization's most valuable asset: its human capital, guaranteeing full compliance with STPS and local authorities.",
            "auto_generated.text_055": "Supervision in High-Risk Projects: On-site monitoring and control of safety protocols in civil works, environmental and industrial projects.",
            "auto_generated.text_056": "Certified Training (STPS): Courses and workshops given by an External Training Agent (ACE) officially registered with the Ministry of Labor.",
            "auto_generated.text_057": "Comprehensive Waste Management (Solid and Hazardous)",
            "auto_generated.text_058": "Water Engineering and Solutions",
            "auto_generated.text_059": "Consulting, Opinions and Legal Compliance",
            "auto_generated.text_060": "Capacity Building",
            "auto_generated.text_061": "Residential Building and Housing",
            "auto_generated.text_062": "Hydraulic and Environmental Infrastructure",
            "auto_generated.text_063": "Project Engineering and Planning",
            "auto_generated.text_064": "Supervision and Construction Control",
            "auto_generated.text_065": "Topographic Surveys and Studies",
            "auto_generated.text_066": "Georeferencing and GPS Precision",
            "auto_generated.text_067": "Digital Modeling and Visualization",
            "auto_generated.text_068": "Construction Control and Supervision",
            "auto_generated.text_069": "Structure and Operational Management (Consulting)",
            "auto_generated.text_070": "Technical Supervision and Field Safety",
            "auto_generated.text_071": "Specialized Training and Education (ACE)",
            "auto_generated.text_072": "Legado\n                            Ambiental",
            "auto_generated.text_073": "<strong>Diagnosis and Characterization: </strong> Solid waste characterization studies, diagnosis and sampling.",
            "auto_generated.text_074": "<strong>Management Plans:</strong> Development of comprehensive management plans for solid and hazardous waste, including classification and tracking.",
            "auto_generated.text_075": "<strong>Logistics and Collection:</strong>Study and optimization of routes and collection methods.",
            "auto_generated.text_076": "<strong>Infrastructure:</strong>Projects for sanitary landfills, organic waste treatment and hazardous waste management works.",
            "auto_generated.text_077": "Get a Quote",
            "auto_generated.text_078": "<strong>Water Treatment:</strong> Design, construction and supervision of wastewater treatment plants.",
            "auto_generated.text_079": "<strong>Water Sustainability:</strong> Alternative recycling or reuse systems, water saving programs and technical saving studies.",
            "auto_generated.text_080": "<strong>Specialized Analysis:</strong> Hydrometeorological studies for planning and prevention.",
            "auto_generated.text_081": "Get a Quote",
            "auto_generated.text_082": "<strong>Impact Assessments:</strong> Environmental impact studies (EsIA), diagnoses and preventive environmental assessments.",
            "auto_generated.text_083": "<strong>Official Documentation:</strong> Preparation of technical reports and environmental opinions with legal validity.",
            "auto_generated.text_084": "Get a Quote",
            "auto_generated.text_085": "<strong>Training:</strong> Courses, workshops and training programs on environmental topics.",
            "auto_generated.text_086": "Get a Quote",
            "auto_generated.text_087": "<strong>Single-Family Housing:</strong> Construction of custom homes and high-end residences.",
            "auto_generated.text_088": "<strong>Multi-Family Housing:</strong> Development of apartment complexes, residential buildings and housing developments.",
            "auto_generated.text_089": "<strong>Turnkey Projects: </strong> Total management from foundation to final finishes.",
            "auto_generated.text_090": "Get a Quote",
            "auto_generated.text_091": "<strong>Wastewater Treatment Plants (WWTP):</strong> Design, construction and commissioning of industrial and municipal treatment systems.",
            "auto_generated.text_092": "<strong>Sanitation Works:</strong> Infrastructure for water reuse and specialized drainage systems.",
            "auto_generated.text_093": "Get a Quote",
            "auto_generated.text_094": "<strong>Development of Executive Projects:</strong> Architectural design, structural calculations, plumbing and electrical installations.",
            "auto_generated.text_095": "<strong>Management of Procedures and Licenses:</strong> Technical support for obtaining construction permits and environmental authorizations.",
            "auto_generated.text_096": "Get a Quote",
            "auto_generated.text_097": "<strong>Technical Supervision of Works:</strong> On-site monitoring to ensure compliance with plans, specifications and material quality.",
            "auto_generated.text_098": "<strong>Cost and Time Control:</strong> Administration of construction schedules (Critical Path) and budgets to prevent deviations.",
            "auto_generated.text_099": "<strong>Construction Audit:</strong> Verification of construction processes and site safety regulations.",
            "auto_generated.text_100": "Get a Quote",
            "auto_generated.text_101": "<strong>Definition</strong> of exact spatial contours and land dimensions for secure foundations.",
            "auto_generated.text_102": "Get a Quote",
            "auto_generated.text_103": "<strong>Location</strong> of precise geospatial coordinates using cutting-edge global technology.",
            "auto_generated.text_104": "Get a Quote",
            "auto_generated.text_105": "<strong>Generation</strong> of three-dimensional (3D) terrain environments for exact volumetric calculations.",
            "auto_generated.text_106": "Get a Quote",
            "auto_generated.text_107": "<strong>Verification</strong> of layouts continuously on real terrain to ensure alignment with planimetry.",
            "auto_generated.text_108": "Get a Quote",
            "auto_generated.text_109": "<strong>Establishment of OHS Departments:</strong> Design, implementation, and comprehensive coordination of Occupational Health and Safety departments.",
            "auto_generated.text_110": "<strong>Regulatory Compliance Audits:</strong> Diagnosis and assurance of current Official Mexican Standards (NOM) (Safety, Health and Organization).",
            "auto_generated.text_111": "<strong>Management of Joint Commissions:</strong> Constitution and training of the Health and Safety Commission (NOM-019-STPS).",
            "auto_generated.text_112": "<strong>Development of Specific Programs:</strong> Safety manuals, civil protection programs and emergency response plans.",
            "auto_generated.text_113": "Get a Quote",
            "auto_generated.text_114": "<strong>Job Hazard Analysis (JHA):</strong>Identification of hazards and risk assessment to prevent occupational accidents and illnesses.",
            "auto_generated.text_115": "<strong>Verification of Equipment and Machinery:</strong> Inspection of safety conditions in tools, scaffolding and heavy machinery.",
            "auto_generated.text_116": "Get a Quote",
            "auto_generated.text_117": "<strong>Issuance of DC-3 Certificates:</strong>Delivery of labor skills documents valid for federal inspections.",
            "auto_generated.text_118": "<strong>Training in High-Risk Jobs:</strong> Specific training in heights, confined spaces, cutting and welding, and handling of chemical substances.",
            "auto_generated.text_119": "<strong>Formation of Emergency Brigades:</strong> First aid, fire prevention and fighting, and building evacuation.",
            "auto_generated.text_120": "Get a Quote",
            "auto_generated.text_121": "<a class=\"inline-flex items-center text-sm font-medium text-gray-300 hover:text-white transition-colors\" href=\"../home.html\">\n<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Home</span>\n</a>",
            "auto_generated.text_122": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Diagnosis and Characterization: </strong> Solid waste characterization studies, diagnosis and sampling.\n                                    </span>",
            "auto_generated.text_123": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Management Plans:</strong> Development of comprehensive management plans for solid and hazardous waste, including classification and tracking.</span>",
            "auto_generated.text_124": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Logistics and Collection:</strong>Study and optimization of routes and collection methods.\n                                    </span>",
            "auto_generated.text_125": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Infrastructure:</strong>Projects for sanitary landfills, organic waste treatment and hazardous waste management works.\n                                    </span>",
            "auto_generated.text_126": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Water Treatment:</strong> Design, construction and supervision of wastewater treatment plants.</span>",
            "auto_generated.text_127": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Water Sustainability:</strong> Alternative recycling or reuse systems, water saving programs and technical saving studies.</span>",
            "auto_generated.text_128": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Specialized Analysis:</strong> Hydrometeorological studies for planning and prevention.</span>",
            "auto_generated.text_129": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Impact Assessments:</strong> Environmental impact studies (EsIA), diagnoses and preventive environmental assessments.</span>",
            "auto_generated.text_130": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Official Documentation:</strong> Preparation of technical reports and environmental opinions with legal validity.</span>",
            "auto_generated.text_131": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Training:</strong> Courses, workshops and training programs on environmental topics.</span>",
            "auto_generated.text_132": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Single-Family Housing:</strong> Construction of custom homes and high-end residences.</span>",
            "auto_generated.text_133": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Multi-Family Housing:</strong> Development of apartment complexes, residential buildings and housing developments.</span>",
            "auto_generated.text_134": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Turnkey Projects: </strong> Total management from foundation to final finishes.</span>",
            "auto_generated.text_135": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Wastewater Treatment Plants (WWTP):</strong> Design, construction and commissioning of industrial and municipal treatment systems.</span>",
            "auto_generated.text_136": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Sanitation Works:</strong> Infrastructure for water reuse and specialized drainage systems.</span>",
            "auto_generated.text_137": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Development of Executive Projects:</strong> Architectural design, structural calculations, plumbing and electrical installations.</span>",
            "auto_generated.text_138": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Management of Procedures and Licenses:</strong> Technical support for obtaining construction permits and environmental authorizations.</span>",
            "auto_generated.text_139": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Technical Supervision of Works:</strong> On-site monitoring to ensure compliance with plans, specifications and material quality.</span>",
            "auto_generated.text_140": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Cost and Time Control:</strong> Administration of construction schedules (Critical Path) and budgets to prevent deviations.</span>",
            "auto_generated.text_141": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Construction Audit:</strong> Verification of construction processes and site safety regulations.</span>",
            "auto_generated.text_142": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Definition</strong> of exact spatial contours and land dimensions for secure foundations.</span>",
            "auto_generated.text_143": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Location</strong> of precise geospatial coordinates using cutting-edge global technology.</span>",
            "auto_generated.text_144": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Generation</strong> of three-dimensional (3D) terrain environments for exact volumetric calculations.</span>",
            "auto_generated.text_145": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Verification</strong> of layouts continuously on real terrain to ensure alignment with planimetry.</span>",
            "auto_generated.text_146": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Establishment of OHS Departments:</strong> Design, implementation, and comprehensive coordination of Occupational Health and Safety departments.</span>",
            "auto_generated.text_147": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Regulatory Compliance Audits:</strong> Diagnosis and assurance of current Official Mexican Standards (NOM) (Safety, Health and Organization).</span>",
            "auto_generated.text_148": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Management of Joint Commissions:</strong> Constitution and training of the Health and Safety Commission (NOM-019-STPS).</span>",
            "auto_generated.text_149": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Development of Specific Programs:</strong> Safety manuals, civil protection programs and emergency response plans.</span>",
            "auto_generated.text_150": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Job Hazard Analysis (JHA):</strong>Identification of hazards and risk assessment to prevent occupational accidents and illnesses.</span>",
            "auto_generated.text_151": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Verification of Equipment and Machinery:</strong> Inspection of safety conditions in tools, scaffolding and heavy machinery.</span>",
            "auto_generated.text_152": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Issuance of DC-3 Certificates:</strong>Delivery of labor skills documents valid for federal inspections.</span>",
            "auto_generated.text_153": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Training in High-Risk Jobs:</strong> Specific training in heights, confined spaces, cutting and welding, and handling of chemical substances.</span>",
            "auto_generated.text_154": "<span class=\"material-symbols-outlined text-primary text-[1rem] mt-0.5\">check_circle</span>\n<span><strong>Formation of Emergency Brigades:</strong> First aid, fire prevention and fighting, and building evacuation.</span>",
            "auto_generated.text_155": "<span class=\"material-symbols-outlined text-[1.2rem]\">dark_mode</span>",
            "auto_generated.text_156": "<span class=\"material-symbols-outlined text-3xl\">menu</span>",
            "auto_generated.text_157": "<span class=\"material-symbols-outlined text-lg\">dark_mode</span>\n<span class=\"text-base font-semibold\" data-i18n=\"nav.theme\">Toggle Theme</span>",
            "auto_generated.text_158": "<span>Get a Quote</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_159": "<span>Get a Quote</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_160": "<span>Get a Quote</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_161": "<span>Get a Quote</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_162": "<span>Get a Quote</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_163": "<span>Get a Quote</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_164": "<span>Get a Quote</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_165": "<span>Get a Quote</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_166": "<span>Get a Quote</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_167": "<span>Get a Quote</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_168": "<span>Get a Quote</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_169": "<span>Get a Quote</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_170": "<span>Get a Quote</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_171": "<span>Get a Quote</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_172": "<span>Get a Quote</span> <span class=\"material-symbols-outlined text-[18px]\">arrow_forward</span>",
            "auto_generated.text_173": "<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Home</span>",
            "auto_generated.text_174": "<span class=\"material-symbols-outlined\">share</span>",
            "auto_generated.text_175": "<span class=\"material-symbols-outlined\">mail</span>",
            "auto_generated.text_176": "Legado\n                            Ambiental",
            "auto_generated.text_177": "<a class=\"inline-flex items-center text-sm font-medium text-gray-700 hover:text-primary dark:text-gray-400 dark:hover:text-white\" href=\"../home.html\">\n<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Home</span>\n</a>",
            "auto_generated.text_178": "<span class=\"material-symbols-outlined text-[1.2rem]\">dark_mode</span>",
            "auto_generated.text_179": "<span class=\"material-symbols-outlined text-3xl\">menu</span>",
            "auto_generated.text_180": "<span class=\"material-symbols-outlined text-lg\">dark_mode</span>\n<span class=\"text-base font-semibold\" data-i18n=\"nav.theme\">Toggle Theme</span>",
            "auto_generated.text_181": "<span data-i18n=\"portfolio_page.load_more\">Load More Projects</span> <span class=\"material-symbols-outlined text-[18px]\">expand_more</span>",
            "auto_generated.text_182": "<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Home</span>",
            "auto_generated.text_183": "<span class=\"material-symbols-outlined\">share</span>",
            "auto_generated.text_184": "<span class=\"material-symbols-outlined\">mail</span>",
            "auto_generated.text_185": "<span data-i18n=\"experience_page.timeline.item1.title\">Environmental Assessment - <strong>Grupo Serla</strong></span>",
            "auto_generated.text_186": "<span data-i18n=\"experience_page.timeline.item2.title\">Sanitation - Tiloxtoc River</span>",
            "auto_generated.text_187": "<span data-i18n=\"experience_page.timeline.item3.title\">Sustainable Tech - <strong>ITESM</strong></span>",
            "auto_generated.text_188": "<span data-i18n=\"experience_page.timeline.item4.title\">High Efficiency WWTP - <strong>IMMSA</strong></span>",
            "auto_generated.text_189": "<span data-i18n=\"experience_page.timeline.item5.title\">Clinical & Hospital Units</span>",
            "auto_generated.text_190": "<span data-i18n=\"experience_page.timeline.item6.title\">Foundation & Civil Works</span>",
            "auto_generated.text_191": "Legado\n              Ambiental",
            "auto_generated.text_192": "<a class=\"inline-flex items-center text-sm font-medium text-gray-300 hover:text-white transition-colors\" href=\"../home.html\">\n<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Home</span>\n</a>",
            "auto_generated.text_193": "<span class=\"material-symbols-outlined text-[1.2rem]\">dark_mode</span>",
            "auto_generated.text_194": "<span class=\"material-symbols-outlined text-3xl\">menu</span>",
            "auto_generated.text_195": "<span class=\"material-symbols-outlined text-lg\">dark_mode</span>\n<span class=\"text-base font-semibold\" data-i18n=\"nav.theme\">Toggle Theme</span>",
            "auto_generated.text_196": "<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Home</span>",
            "auto_generated.text_197": "<span class=\"material-symbols-outlined\">share</span>",
            "auto_generated.text_198": "<span class=\"material-symbols-outlined\">mail</span>",
            "auto_generated.text_199": "Legado\n                            Ambiental",
            "auto_generated.text_200": "<a class=\"inline-flex items-center text-sm font-medium text-gray-300 hover:text-white transition-colors\" href=\"../home.html\">\n<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Home</span>\n</a>",
            "auto_generated.text_201": "<span class=\"material-symbols-outlined text-primary w-10 h-10 bg-primary/10 rounded-xl flex items-center justify-center w-full sm:w-auto justify-center\">call</span>\n<span data-i18n=\"contact_page.info.phone1\">+52 55 7312 6918</span>",
            "auto_generated.text_202": "<span class=\"material-symbols-outlined text-primary w-10 h-10 bg-primary/10 rounded-xl flex items-center justify-center w-full sm:w-auto justify-center\">call</span>\n<span data-i18n=\"contact_page.info.phone2\">+52 72 2672 7212</span>",
            "auto_generated.text_203": "<span class=\"material-symbols-outlined text-primary w-10 h-10 bg-primary/10 rounded-xl flex items-center justify-center w-full sm:w-auto justify-center\">mail</span>\n<span data-i18n=\"contact_page.info.email\"><strong>legado.ambiental.mx@gmail.com</strong></span>",
            "auto_generated.text_204": "<span class=\"material-symbols-outlined text-primary w-10 h-10 bg-primary/10 rounded-xl flex items-center justify-center w-full sm:w-auto justify-center\">location_on</span>\n<span data-i18n=\"contact_page.info.addr\">U.H. Valle de Ecatepec, <br/> C.P. 55119, Ecatepec, State of Mexico</span>",
            "auto_generated.text_205": "<span class=\"material-symbols-outlined text-[1.2rem]\">dark_mode</span>",
            "auto_generated.text_206": "<span class=\"material-symbols-outlined text-3xl\">menu</span>",
            "auto_generated.text_207": "<span class=\"material-symbols-outlined text-lg\">dark_mode</span>\n<span class=\"text-base font-semibold\" data-i18n=\"nav.theme\">Toggle Theme</span>",
            "auto_generated.text_208": "<span class=\"material-symbols-outlined text-lg mr-2\">home</span>\n<span data-i18n=\"nav.home\">Home</span>",
            "auto_generated.text_209": "<span class=\"material-symbols-outlined\">share</span>",
            "auto_generated.text_210": "<span class=\"material-symbols-outlined\">mail</span>",
            "auto_generated.text_211": "© 2024 Legado Ambiental. <span data-i18n=\"footer.rights\"><strong>© {{year}} Legado Ambiental S.A. de C.V. <br/>All rights reserved.</strong></span>",
            "auto_generated.text_212": "<span class=\"material-symbols-outlined text-xl\">dark_mode</span>",
            "auto_generated.text_213": "<span class=\"material-symbols-outlined\">home</span>\n<span data-i18n=\"error_404.btn\">Back to Home</span>"
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
    // 1. Check for exact match first
    if (obj && obj[path]) return obj[path];

    // 2. Try normal dot notation traversal
    const parts = path.split('.');
    let val = parts.reduce((acc, part) => acc && acc[part], obj);
    if (val) return val;

    // 3. Fallback: Check if the category exists and contains the full path as a key
    // This supports auto-generated keys like data-i18n="auto_generated.text_057"
    if (parts.length > 0 && obj && obj[parts[0]] && obj[parts[0]][path]) {
        return obj[parts[0]][path];
    }

    return undefined;
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
        let text = getValueByPath(translationsData, key);
        if (text && typeof text === "string") { text = text.replace("{{year}}", new Date().getFullYear()); }

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
        let text = getValueByPath(translationsData, key);
        if (text && typeof text === "string") { text = text.replace("{{year}}", new Date().getFullYear()); }
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
            btn.classList.add('text-primary', 'font-bold');
            btn.classList.remove('text-gray-500', 'dark:text-gray-400', 'font-normal');
        } else {
            btn.classList.remove('text-primary', 'font-bold');
            btn.classList.add('text-gray-500', 'dark:text-gray-400', 'font-normal');
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

        // Global Unobtrusive Event Handlers
        const actionBtn = e.target.closest('[data-action]');
        if (actionBtn) {
            const action = actionBtn.getAttribute('data-action');
            if (action === 'toggle-theme') {
                if (typeof window.toggleDarkMode === 'function') {
                    window.toggleDarkMode();
                } else if (typeof globalThis.toggleDarkMode === 'function') {
                    globalThis.toggleDarkMode();
                }
            } else if (action === 'copy-url') {
                navigator.clipboard.writeText(window.location.href);
                alert('URL copiada');
            } else if (action === 'smooth-scroll-contact') {
                const tabBtn = document.getElementById('tab-btn-1');
                const tabSec = document.getElementById('tab-section-1');
                if (tabBtn && tabSec) {
                    tabBtn.click();
                    tabSec.scrollIntoView({ behavior: 'smooth' });
                }
            } else if (action === 'navigate') {
                window.location.href = actionBtn.getAttribute('data-href');
            } else if (action === 'navigate-blank') {
                window.open(actionBtn.getAttribute('data-href'), '_blank');
            }
        }
    });


    // Global Loader logic
    window.addEventListener('load', () => {
        const loader = document.getElementById('global-loader');
        if (loader) {
            loader.classList.add('opacity-0');
            setTimeout(() => {
                loader.style.display = 'none';
            }, 700);
        }
    });
});
