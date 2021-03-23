# What are sets?
# A set is similar to a list but it is unordered
# Sets are mutable
# {} is ued to create a set
car_parts = {'doors', 'windows', 'tires'}
print(car_parts)

# What are Frozen sets?
# An iterable made immutable
car_parts = {'doors', 'windows', 'tires'}
frozen = frozenset(car_parts)
print(frozen)
