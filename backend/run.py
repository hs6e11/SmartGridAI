from app import create_app
from app.config import DevelopmentConfig, ProductionConfig, TestingConfig

# Choose the appropriate configuration class based on your environment
# For example, use DevelopmentConfig for development
app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    app.run()

