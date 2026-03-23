from pages.dashboard_page import DashboardPage

def test_dashboard(login):
    dashboard = DashboardPage(login)
    data = dashboard.get_dashboard_counts()

    print("\nDashboard Data:\n", data)

    assert len(data) > 0