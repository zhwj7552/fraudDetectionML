import random

from fixtures import USERS_FIXTURE


def get_data():
    """
    I don't want to keep
    """
    return USERS_FIXTURE

def generate_data():
    results = []
    for d in xrange(1000):
        age = random.randint(2, 50)
        email = generate_email()

        h24_success = age / random.randint(1, age)
        data = {
            'user': {
                'age': age,  # days on website
                'email': email,
                'country': 'israel',
            },
            'loginHistory': {
                '24hoursSuccess': h24_success,
                '30daysSuccess': age/5 + random.randint(1,5),
                '24hoursFailed': h24_success/7,
                '30daysFailed': random.randint(h24_success/2, h24_success+age/2),
            },
            # 'browser': {
            #     'userAgents': [
            #         'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            #         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'
            #     ],
            # },
        }
        results.append(data)
    return results


def generate_email():
    """
    Just a random email
    """
    first_names = ['linden', 'truman', 'helbert', 'andy', 'renwick']
    domains = ['gmail.com', 'yahoo.com', 'walla.co.il', 'aol.com', 'outlook.com']
    return '{first_name}@{domain}'.format(first_name=random.choice(first_names), domain=random.choice(domains))


def parse_to_flat_features(data):
    """
    For now I use only 2 features, can add more easly.
    """
    results = []
    for item in data:
        results.append([
            item['user']['age'],
            item['loginHistory']['30daysSuccess'],
        ])
    return results

if __name__ == '__main__':
    print list(get_data())
