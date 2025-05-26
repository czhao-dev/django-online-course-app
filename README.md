# Online Course App - Final Django Project

This project is the final implementation of an **Online Course App**, developed using Django. It is based on a boilerplate template provided as part of a course, with improvements and features added as per the project specifications.

## Features Implemented

The following features and enhancements were implemented in this project:

1. **Models Implementation**
   - Created `Question`, `Choice`, and `Submission` models.

2. **Admin Interface Enhancements**
   - Registered the new models in the Django admin site.
   - Created a new `Course` object with exam-related models using the admin interface.

3. **Template Updates**
   - Updated the **Course Details** template to display questions and choices dynamically.

4. **Exam Result Functionality**
   - Created a new **Exam Result** template to show the result of a submission.
   - Implemented a view to submit and evaluate exam results.
   - Developed a view to display the final exam result.

## Technologies Used

- Python 3.x
- Django Web Framework
- HTML/CSS (Templates)
- SQLite (default Django database)
- Django Admin Interface

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/online-course-app.git
   cd online-course-app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser to access the admin site:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the site at `http://127.0.0.1:8000/` and the admin interface at `http://127.0.0.1:8000/admin/`

## License

This project is provided as part of an academic course and is intended for educational purposes.
