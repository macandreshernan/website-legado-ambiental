import React from 'react';
import PropTypes from 'prop-types';

// Design System / Token Simulation based on requirements
// theme object removed as it was unused

const services = [
    {
        id: 1,
        title: 'Gestión de Residuos',
        description: 'Soluciones integrales para la recolección, transporte y disposición final de residuos industriales y urbanos.',
        icon: 'delete_sweep'
    },
    {
        id: 2,
        title: 'Tratamiento de Agua',
        description: 'Diseño e implementación de plantas de tratamiento y sistemas de purificación para recuperación de recursos hídricos.',
        icon: 'water_drop'
    },
    {
        id: 3,
        title: 'Consultoría Técnica',
        description: 'Asesoría especializada en normativa ambiental, estudios de impacto y optimización de procesos sostenibles.',
        icon: 'engineering'
    }
];

const ServiceCard = ({ title, description, icon }) => {
    return (
        <div className="group relative bg-white rounded-2xl p-8 border border-gray-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 overflow-hidden">
            {/* Decorative Background Element */}
            <div className="absolute top-0 right-0 w-32 h-32 bg-gray-50 rounded-bl-full -mr-8 -mt-8 transition-transform group-hover:scale-150 group-hover:bg-primary/10"></div>

            {/* Icon Container */}
            <div className="relative mb-6 inline-flex items-center justify-center w-16 h-16 rounded-xl bg-primary/10 text-primary group-hover:bg-primary group-hover:text-white transition-colors duration-300">
                <span className="material-symbols-outlined text-3xl">{icon}</span>
            </div>

            {/* Content */}
            <h3 className="relative text-xl font-bold text-navy mb-3 font-serif group-hover:text-primary transition-colors">
                {title}
            </h3>
            <p className="relative text-gray-600 text-sm leading-relaxed mb-6 font-sans">
                {description}
            </p>

            {/* Action Link */}
            <a href="javascript:void(0)" rel="noopener noreferrer" className="relative inline-flex items-center text-sm font-bold text-primary group-hover:text-primaryDark transition-colors">
                <span>Conocer más</span>
                <span className="material-symbols-outlined text-sm ml-2 transform group-hover:translate-x-1 transition-transform">
                    arrow_forward
                </span>
            </a>
        </div>
    );
};

ServiceCard.propTypes = {
    title: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    icon: PropTypes.string.isRequired,
};

const ServicesSection = () => {
    return (
        <section className="py-20 bg-background-light">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-16 max-w-3xl mx-auto">
                    <span className="text-primary font-bold tracking-widest uppercase text-sm mb-2 block font-sans">
                        Nuestros Servicios
                    </span>
                    <h2 className="text-4xl md:text-5xl font-black text-navy mb-6 font-serif">
                        Soluciones para un Futuro Sostenible
                    </h2>
                    <p className="text-lg text-gray-600 font-sans">
                        Combinamos ingeniería de vanguardia con conciencia ambiental para ofrecer resultados que perduran.
                    </p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                    {services.map(service => (
                        <ServiceCard
                            key={service.id}
                            {...service}
                        />
                    ))}
                </div>
            </div>
        </section>
    );
};

export default ServicesSection;
