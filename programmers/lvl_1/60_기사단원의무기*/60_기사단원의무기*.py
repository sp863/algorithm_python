def get_prime_count(number):
    count = 0

    for i in range(1, int(number**(1/2))+1):
        if number % i == 0:
            count += 1
            if i**2 != number:
                count += 1

    return count


def solution(number, limit, power):
    prime_count = [get_prime_count(i) for i in range(1, number+1)]

    return sum([num if num <= limit else power for num in prime_count])

# Solution


def cf(n):
    a = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            a.append(n//i)
            a.append(i)
    return len(set(a))


def solution(number, limit, power):
    return sum([cf(i) if cf(i) <= limit else power for i in range(1, number+1)])

# in my solution I don't understand why I'm checking for this condition (if i**2 != number: count += 1)
