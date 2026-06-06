from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    # 1. Launch browser maximized
    browser = play.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    page.goto("https://react-library-frontend-henna.vercel.app/student-login")

    admission_number = page.wait_for_selector('input[name="admissionNumber"]')
    admission_number.fill('ADM101')
    page.wait_for_timeout(2000)

    username = page.wait_for_selector('input[name="username"]')
    username.fill('navas123')
    page.wait_for_timeout(2000)

    password = page.wait_for_selector('input[name="password"]')
    password.fill('Abc@1234')

    eyebutton = page.wait_for_selector('svg[class="lucide lucide-eye-off"]')
    eyebutton.click()

    login_button = page.wait_for_selector(
        'button[class="jsx-5df7a5588ea39e0a w-full py-3.5 rounded-md font-extrabold text-white text-sm bg-gradient-to-r from-indigo-500 to-violet-500 hover:from-indigo-600 hover:to-violet-600 shadow-lg shadow-indigo-200 hover:-translate-y-0.5 hover:shadow-xl disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-y-0 transition-all duration-200 flex items-center justify-center gap-2 mb-4"]')
    login_button.click()
    page.wait_for_timeout(2000)
    page.goto("https://react-library-frontend-henna.vercel.app/student/worldsmith")
    page.wait_for_timeout(2500)

    # WORLD SMITH
    story_title = page.wait_for_selector('input[placeholder="Give your story a captivating title..."]')
    story_title.type('The test Heading added for your story')
    story_content = page.wait_for_selector('textarea[placeholder="Start writing your masterpiece here... Let your creativity flow ✨"]')
    story_content.type('The test data long data added for your masterpiece testing data added \n ok for the'
                       ' purpose of testing . \n The long data added for the purpose of your masterpiece '
                       '\n Purpose of the data added for the Temp \n The test data added for the purpose of your masterpiece'
                       '\n We the purpose of testing and the test data added for the purpose of your masterpiece'
                       '\n Quest the founder of foreign science and technology and the test'
                       '\n We the people are responsible '
                       '\n Thank you')
    # 1. Locate the container element that has the inner scrollbar
    inner_container = page.locator('input[placeholder="Give your story a captivating title..."]')
    # 2. Hover the mouse over it so the browser knows where to scroll
    inner_container.hover()
    # 3. Scroll down 500 pixels inside that container
    page.mouse.wheel(delta_x=0, delta_y=500)
    click_submit=page.wait_for_selector('button[class="flex-1 sm:flex-none px-4 sm:px-8 py-2 sm:py-3 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-full transition-all duration-200 font-medium text-xs sm:text-sm shadow-lg flex items-center justify-center gap-1.5 sm:gap-2 hover:from-purple-700 hover:to-pink-700 hover:shadow-xl hover:scale-105"]')
    click_submit.click()
    page.wait_for_timeout(5000)