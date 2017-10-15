from model import User


def validate(username, password, first_name, last_name, email):
    if username is None:
        print "Username is required"
        return 'Username is required', 400

    if password is None:
        print "Password is required"
        return 'Password is required', 400

    if first_name is None:
        print "First name is required"
        return 'First name is required', 400

    if last_name is None:
        print "Last name is required"
        return 'Last name is required', 400

    user = User.query.filter_by(username=username).first()
    if user is not None:
        print 'Duplicate!'
        return 'Username already exists', 409

    if email is not None:
        user = User.query.filter_by(email=email).first()
        if user is not None:
            print 'Duplicate!'
            return 'Email already exists', 409
