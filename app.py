from flask import Flask
FI=Flask(__name__)


@FI.route('/wish')
def wish():
    return 'normal view is completed'


@FI.route('/venky')
def venky():
    return 'flask is success '

if __name__=='__main__':
    FI.run(debug=True)