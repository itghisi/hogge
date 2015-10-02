#-*- coding: utf8
from hogge.htmltimesheetwriter import HtmlTimeSheetWriter
from hogge.sessiontimesheet import SessionTimeSheet
import os


def test_htmldashboardwriter():
    test_dirname = os.path.dirname(__file__)
    timesheet = SessionTimeSheet.create_default_timesheet()
    timesheet.add_lap(dict(Lap=1, LapLastLapTime=68.392, FuelLevel=12.0))
    timesheet.add_lap(dict(Lap=2, LapLastLapTime=69.584, FuelLevel=11.2))

    writer = HtmlTimeSheetWriter("test", test_dirname)
    writer.dump(timesheet)