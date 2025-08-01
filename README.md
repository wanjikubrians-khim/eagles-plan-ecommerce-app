# Eagles Plan E-commerce Application

A modern, production-ready Django e-commerce application with comprehensive features for online retail.

![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![Django](https://img.shields.io/badge/django-v4.2.11-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-Production%20Ready-success.svg)

## 🚀 Features

### 🛍️ Core E-commerce Features
- **Product Management**: Categories, products with variants, inventory tracking
- **Shopping Cart**: Session-based cart with persistent storage
- **Order Management**: Complete order lifecycle with payment integration ready
- **User Accounts**: Registration, profiles, address management
- **Product Reviews**: Customer reviews and ratings system
- **Inventory Tracking**: Stock levels with low stock warnings
- **Sale System**: Products with sale prices and discount calculations

### 🔐 Security & Authentication
- **Django Allauth**: Comprehensive authentication system
- **Security Headers**: CSRF, XSS, and clickjacking protection
- **Environment Variables**: Secure configuration management
- **Session Management**: Database-backed sessions for production

### 📱 Modern UI/UX
- **Responsive Design**: Mobile-first responsive layouts
- **Bootstrap 5**: Modern, accessible UI components
- **Crispy Forms**: Enhanced form rendering
- **AOS Animations**: Smooth scroll animations
- **Font Awesome**: Professional icons

### 🚀 Production Ready
- **Docker Support**: Containerized deployment
- **Database Flexibility**: SQLite for development, PostgreSQL for production
- **Static File Handling**: WhiteNoise for static files
- **Logging**: Comprehensive logging configuration
- **Caching**: Redis caching for improved performance
- **SEO Ready**: Meta tags, slugs, and structured URLs

## 📦 Installation & Setup

### Prerequisites
- Python 3.9+
- pip
- virtualenv (recommended)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/eagles-plan-ecommerce-app.git
   cd eagles-plan-ecommerce-app
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env with your configuration
   # Generate a new SECRET_KEY for production!
   ```

5. **Run database setup**
   ```bash
   cd ecommerce_project
   python manage.py migrate
   python manage.py populate_db  # Load sample data
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000` to see your application!

## 🌐 Application URLs

- **Main Website**: http://127.0.0.1:8000
- **Admin Panel**: http://127.0.0.1:8000/admin
- **Product Categories**: `/category/<slug>/`
- **Product Details**: `/product/<slug>/`
- **Shopping Cart**: `/cart/`
- **Orders**: `/orders/`
- **User Accounts**: `/accounts/`

## 📁 Project Structure

```
eagles-plan-ecommerce-app/
├── ecommerce_project/
│   ├── accounts/                 # User management app
│   │   ├── models.py            # Profile, Address models
│   │   ├── views.py             # User profile views
│   │   ├── forms.py             # User forms
│   │   └── admin.py             # Admin configuration
│   ├── ecommerce_app/           # Main shop app
│   │   ├── models.py            # Product, Category, Review models
│   │   ├── views.py             # Shop views
│   │   ├── cart.py              # Shopping cart logic
│   │   ├── admin.py             # Admin configuration
│   │   ├── templates/           # HTML templates
│   │   ├── static/              # CSS, JS, images
│   │   └── management/          # Custom Django commands
│   ├── orders/                  # Order management app
│   │   ├── models.py            # Order, OrderItem models
│   │   ├── views.py             # Order views
│   │   └── admin.py             # Admin configuration
│   ├── ecommerce_project/       # Project settings
│   │   ├── settings.py          # Main settings file
│   │   ├── urls.py              # URL configuration
│   │   └── wsgi.py              # WSGI configuration
│   ├── media/                   # User uploaded files
│   ├── staticfiles/             # Collected static files
│   └── manage.py                # Django management script
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
├── Dockerfile                   # Docker configuration
└── README.md                    # This file
```

## ⚙️ Configuration

### Environment Variables

Key environment variables to configure in `.env`:

```bash
# Security
SECRET_KEY=your-secret-key-here
DEBUG=False  # Set to False in production
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Payment (Stripe)
STRIPE_PUBLISHABLE_KEY=pk_live_your_key
STRIPE_SECRET_KEY=sk_live_your_key

# Caching
REDIS_URL=redis://localhost:6379/0
```

### Sample Data

The application includes a management command to populate the database with sample data:

```bash
python manage.py populate_db --clear  # Clear existing data and populate
python manage.py populate_db          # Add sample data without clearing
```

This creates:
- 4 product categories
- 11 sample products with real pricing
- 3 sample users with profiles
- 4 product reviews

## 🐳 Docker Deployment

1. **Build the image**
   ```bash
   docker build -t eagles-plan-ecommerce .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 --env-file .env eagles-plan-ecommerce
   ```

## 🚀 Production Deployment

### Prerequisites for Production
1. Set `DEBUG=False` in environment variables
2. Configure proper `ALLOWED_HOSTS`
3. Use PostgreSQL database
4. Set up Redis for caching
5. Configure email settings
6. Set up SSL certificates

### Deployment Steps
1. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

2. **Run migrations**
   ```bash
   python manage.py migrate
   ```

3. **Use a production WSGI server**
   ```bash
   gunicorn ecommerce_project.wsgi:application
   ```

## 🛠️ Development

### Management Commands

- `python manage.py populate_db` - Populate database with sample data
- `python manage.py clear_sessions` - Clear all user sessions
- `python manage.py collectstatic` - Collect static files

## 📊 Admin Features

The admin panel provides comprehensive management:

- **Products**: Full CRUD with bulk actions, filtering, search
- **Categories**: Organize products with SEO fields
- **Users**: Extended user profiles with addresses
- **Orders**: Order management and tracking
- **Reviews**: Approve/manage customer reviews

Access admin at `/admin/` with superuser credentials.

## 🔄 Version History

### Version 2.0.0 (Current) - Production Ready
- ✅ Complete production-ready architecture
- ✅ Enhanced user management with profiles and addresses
- ✅ Full order management system
- ✅ Professional admin interface with bulk actions
- ✅ Comprehensive security enhancements
- ✅ Docker containerization support
- ✅ Advanced logging and monitoring
- ✅ Performance optimizations with caching
- ✅ SEO-ready models and URLs
- ✅ Responsive design with modern UI
- ✅ Product reviews and ratings system
- ✅ Inventory management with stock tracking
- ✅ Sale pricing and discount system

### Version 1.0.0 - Basic Functionality
- Basic e-commerce functionality
- Simple product catalog
- Basic shopping cart
- Simple checkout process

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Support

For support and questions:
- Create an issue on GitHub
- Email: support@eaglesplan.com

---

**Eagles Plan E-commerce Application** - Built with ❤️ using Django
