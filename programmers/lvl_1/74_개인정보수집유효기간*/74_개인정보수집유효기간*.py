def find_deadline(collected, months):
    date = collected.split('.')

    year = int(date[0])
    month = int(date[1])
    day = int(date[2])

    month += months
    if month > 12:
        month -= 12
        year += 1

    return [year, month, day]


def isPast(today, deadline):
    year, month, day = today
    year_dead, month_dead, day_dead = deadline

    if year > year_dead:
        return True
    if year == year_dead and month > month_dead:
        return True
    if year == year_dead and month == month_dead and day >= day_dead:
        return True

    return False


def solution(today, terms, privacies):
    terms_obj = {term.split(' ')[0]: (
        int(term.split(' ')[1])) for term in terms}
    today = list(map(int, today.split('.')))
    answer = []

    for index, privacy in enumerate(privacies):
        collected = privacy.split(' ')[0]
        cat = privacy.split(' ')[1]

        deadline = find_deadline(collected, terms_obj[cat])

        if isPast(today, deadline):
            answer.append(index + 1)

    return answer


# Solution

def dateToDay(date):
    year, month, day = map(int, date.split("."))
    return (year * 12 * 28) + (month * 28) + day


def solution(today, terms, privacies):
    answer = []

    # today
    today = dateToDay(today)

    # terms
    termsInfo = dict()
    for term in terms:
        term = term.split()
        termsInfo[term[0]] = int(term[1]) * 28

    # privacies
    for i in range(len(privacies)):
        date, term = privacies[i].split()
        if dateToDay(date) + termsInfo[term] <= today:
            answer.append(i+1)

    return answer


def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day


def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire

# my solution is incorrect.
# need to solve this problem again.
# both solutions turn the dates into days and compare them.
