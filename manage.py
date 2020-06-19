#!/usr/bin/env python
from app import app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def generate_fake():
    sql_file = open('generate_fake.sql', 'r', encoding='utf-8')
    sql_command = ''
    for line in sql_file:
        if not line.startswith('--') and line.strip('\n'):
            sql_command += line.strip('\n')
            if sql_command.endswith(';'):
                try:
                    db.session.execute(sql_command)
                    db.session.commit()
                except:
                    print('Ops')
                finally:
                    sql_command = ''
    print("[Info]:Generate fake info Done!")


if __name__ == '__main__':
    manager.run()
