from hogge.sessiondashboard import SessionDashboard
from hogge.xlsdashboardwriter import XlsDashboardWriter


def test_xlsdashboardwriter(tmpdir):
    xls_file = tmpdir.mkdir("hogge").join("session.xlsx")

    dashboard = SessionDashboard.create_default_dashboard()
    dashboard.add_lap(dict(Lap=1, LapLastLapTime=68.392, FuelLevel=12.0))
    dashboard.add_lap(dict(Lap=2, LapLastLapTime=69.584, FuelLevel=11.2))

    writer = XlsDashboardWriter(str(xls_file))
    writer.write(dashboard)