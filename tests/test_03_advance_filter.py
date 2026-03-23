from pages.filter_page import FilterPage

def test_filter(login):
    filter_page = FilterPage(login)

    filter_page.open_filter()
    filter_page.clear_filter()
    filter_page.select_claim_type("Authorisation")
    filter_page.apply_filter()

    count = filter_page.get_count()

    print("Count:", count)

    assert count >= 0