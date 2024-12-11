# Educational Support Assistant

This assistant is designed to function as an educational support tool, aimed at assisting institutions in analyzing student data and identifying patterns of dropout risk based on the information provided by the institution's database.

## Features

- **Data Analysis**: Processes and analyzes student data to detect trends and insights.
- **Dropout Risk Prediction**: Identifies patterns associated with dropout risks using the provided institutional data.
- **Customizable Integration**: Works with different database formats for seamless integration with institutional systems.

## Requirements

- **Database Access**: The tool requires access to the institution's database for data processing.
- **Environment**:
  - **Programming Language**: Python
  - **Libraries**:
    - Flask==2.3.0
    - Flask-SQLAlchemy==2.5.1
    - Flask-Cors==3.0.10
    - Werkzeug==2.3.0
    - mysql-connector-python==9.1.0
    - sentence-transformers==3.3.1
    - qdrant-client==1.12.1
    - openai==1.55.3

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Johnymonteiiro/ai_school_assistent
   ```

2. Navigate to the project directory:

   ```bash
   cd ai_school_assistent
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure your `requirements.txt` includes the following:

   ```text
   Flask==2.3.0
   Flask-SQLAlchemy==2.5.1
   Flask-Cors==3.0.10
   Werkzeug==2.3.0
   mysql-connector-python==9.1.0
   sentence-transformers==3.3.1
   qdrant-client==1.12.1
   openai==1.55.3
   ```

4. Configure the database connection in the `.env` file:

   ```env
   DATABASE_URL=your-database-url
   ```

## Usage

1. Start the assistant:

   ```bash
   python app.py
   ```

2. Provide the necessary database access credentials.

3. Use the interface to upload or select data for analysis.

4. View the generated reports and dropout risk patterns in the output section.

## Contributing

We welcome contributions to enhance the functionality of this tool. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:

   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add feature-name"
   ```

4. Push your changes and open a pull request:

   ```bash
   git push origin feature-name
   ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For questions or support, please contact [johnymonteiiro@gmail.com].

