from playwright.sync_api import sync_playwright

def get_month_listeners(id_artist):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()

        page = context.new_page()
        page.goto(f"https://open.spotify.com/artist/{id_artist}")

        page.wait_for_selector('span[class="Ydwa1P5GkCggtLlSvphs"]')
        monthListeners = page.query_selector('span[class="Ydwa1P5GkCggtLlSvphs"]')
        listeners = monthListeners.inner_text()
        format_listeners = listeners.split(" ")[0].replace(",", ".")        

        page.wait_for_selector('h1[class="Type__TypeElement-sc-goli3j-0 fLMRCf"]')
        artist_name = page.query_selector('h1[class="Type__TypeElement-sc-goli3j-0 fLMRCf"]').inner_text()
        
        page.wait_for_selector('img[class="mMx2LUixlnN_Fu45JpFB CmkY1Ag0tJDfnFXbGgju _EShSNaBK1wUIaZQFJJQ ta4ePOlmGXjBYPTd90lh Yn2Ei5QZn19gria6LjZj"]')
        artist_img = page.query_selector('img[class="mMx2LUixlnN_Fu45JpFB CmkY1Ag0tJDfnFXbGgju _EShSNaBK1wUIaZQFJJQ ta4ePOlmGXjBYPTd90lh Yn2Ei5QZn19gria6LjZj"]').get_attribute("src")
        

        browser.close()

        return {
            "artistName": artist_name,
            "listeners": format_listeners, 
            "artistImage": artist_img
        }

