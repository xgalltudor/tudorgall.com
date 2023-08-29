import os	
from robot import run	

def run_robot_tests():	
    os.environ['PATH'] += os.pathsep + 'C:\WebDrivers\chromedriver.exe'	
    run('Tests',	
        report='Results/report.html',	
        log='Results/log.html',	
        output='Results/output.xml')	


if __name__ == '__main__':	
    run_robot_tests()	
