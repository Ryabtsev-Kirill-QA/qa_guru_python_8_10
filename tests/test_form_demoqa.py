from qa_guru_python_8_10.pages.registration_page import RegistrationPage


def test_form_demoqa():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Test_Name')
    registration_page.fill_last_name('Test_Last_Name')
    registration_page.fill_email('test@gmail.com')
    registration_page.choose_gender('1')
    registration_page.fill_mobile_number('8800555353')
    registration_page.fill_date_of_birth('2000', 'December', '11')
    registration_page.fill_subjects('Computer Science')
    registration_page.choose_hobbies('1')
    registration_page.upload_picture('foto.jpg')
    registration_page.fill_current_address('Test_Adress, 9')
    registration_page.select_state('NCR')
    registration_page.select_city('Delhi')
    registration_page.submit_form()

    # THEN
    registration_page.should_have_registered_user_with(
        'Test_Name Test_Last_Name',
        'test@gmail.com',
        'Male',
        '8800555353',
        '11 December,2000',
        'Computer Science',
        'Sports',
        'foto.jpg',
        'Test_Adress, 9',
        'NCR Delhi'
    )
