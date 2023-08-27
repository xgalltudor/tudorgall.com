from robot import run

def run_robot_tests():
    run('Tests',
        report='Results/report.html',
        log='Results/log.html',
        output='Results/output.xml')

if __name__ == '__main__':
    run_robot_tests()
