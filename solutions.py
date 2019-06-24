#Maor Yatskan 301791380
#Anna Rogozin 323686477
from functools import reduce
import json


class Collection(object):

    # str, map, list, tuple, set , range (except dict)
    def __init__(self, iterable=None):
        """return Collection object, holds it's iterable as tuple."""
        if type(iterable) is dict:
            list1 = list()
            list1.append(iterable)
            self.iterable = tuple(list1)
        elif iterable is None:
            self.iterable = tuple()
        else:
            self.iterable = tuple(iterable)

    def first(self):
        """return a copy of the first item stored in the internal collection."""
        if len(self.iterable) == 0:
            return None
        else:
            cp = self.iterable[0]
            return cp

    def last(self):
        """return a copy of the last item stored in the internal collection."""
        if self.iterable == 0:
            return None
        else:
            cp = self.iterable[-1]
            return cp

    def take(self, amount):
        """return a new Collection contain a subset of the original items."""
        if amount > len(self.iterable):
            amount = len(self.iterable)
        return Collection(self.iterable[:amount])

    def append(self, *elements):
        """return a new Collection with the new elements appended to the end."""
        new_iterable = list(self.iterable)
        for i in range(len(elements)):
            new_iterable.append(elements[i])
        return Collection(new_iterable)

    def prepend(self, *elements):
        """return a new Collection with the new elements appended at the beginning."""
        return Collection(elements).append(self.iterable)

    def filter(self, *callbacks):
        """return a new filtered Collection."""
        temp = list(self.iterable)
        for callback in callbacks:
            try:
                temp = list(filter(callback, temp))
            except TypeError:
                pass
        return Collection(temp)

    def map(self, *callbacks):
        """return a new mapped Collection."""
        temp = list(self.iterable)
        for callback in callbacks:
            temp = list(map(callback, temp))
        return Collection(temp)

    def reduce(self, callback, initial=0):
        """return reduced value of the collection."""
        return reduce(callback, list(self.iterable), initial)

    def sort(self, key=None, reversed=False):
        """return a new sorted collection based on the key provided
            If no key was provided, the collection should be sorted using standard sorting strategies."""
        temp = list(self.iterable)
        func = None
        if type(key) is str:
            func = lambda x: x.get(key)
        elif key is None and type(self.iterable[0]) is dict:
            first_key = next(iter(self.iterable[0]))
            func = lambda x: x.get(first_key)
        temp = sorted(temp, key=func, reverse=reversed)
        return Collection(temp)

    def set(self, position, value):
        """return a new Collection while setting the value at the position provided."""
        temp = list(self.iterable)
        if position < len(temp):
            temp[position] = value
        return Collection(temp)

    def pluck(self, key):
        """return a new Collection of the dictionary keys (only if the collection contain dictionary,
        otherwise return copy of the object)"""
        temp = []
        for item in self.iterable:
            if type(item) is dict:
                temp.append(item.get(key))
        if len(temp) == 0:
            return Collection(self.iterable)
        else:
            return Collection(temp)

    def values(self):
        """return a copy of the internal values"""
        temp = []
        for item in self.iterable:
            if '__len__' in dir(item):
                if len(item) == 1:
                    temp.append(item)
                else:
                    for element in item:
                        temp.append(element)
            else:
                temp.append(item)
        return tuple(temp)

    def unique(self):
        """return a new collection that contains the unique items."""
        return Collection(set(self.iterable))

    def tap(self, callback):
        """pass each element of the collection by-value to a callback function."""
        for i in range(len(self.iterable)):
            callback(self.iterable[i])

    def __getitem__(self, position):
        """return the item at a given position . If the position provided does not exist, None should be returned."""
        length = len(self.iterable)
        if not length == 0:
            position = position % length
            if position in range(length):
                return self.iterable[position]
        return None

    def __add__(self, other):
        """return a new Collection contain the concatenated collections"""
        if type(other) is Collection:
            return Collection((self.iterable + other.iterable))
        else:
            return self + Collection(other)

    def __sub__(self, other):
        """return a new Collection containing items that exist in the first collection but not in the second"""
        if type(other) is Collection:
            set1 = set(self.iterable)
            set2 = set(other.iterable)
            return Collection(set1 - set2)
        else:
            return self - Collection(other)

    def __len__(self):
        """return the length of the Collection"""
        return len(tuple(self.iterable))

    def __contains__(self, element):
        """return the existence of an element in the Collection"""
        return element in self.iterable

    def __eq__(self, other):
        """return the whether all the elements of the two Collection s are equal"""
        if len(self) == len(other):
            for x, y in zip(self.iterable, other.iterable):
                if not x == y:
                    return False
            return True
        else:
            return False

    def __ne__(self, other):
        """return the whether all the elements of the two Collection  are not equal"""
        return not self.__eq__(other)

    def __str__(self):
        """return a string representation of the elements of the object"""
        return self.iterable.__str__()

    def __repr__(self):
        """return a programatic representation of the elements of the object"""
        return "Collection(" + self.iterable.__str__() + ")"


def enumerate_waze(filename):
    """return a new collection contain the dictionary stored in the  json file"""
    with open(filename, 'r') as f:
        return Collection(json.load(f))


def clean_noise(c_out):
    """return a new collection contain only dictionaries that have "reliability" ,"country" and "user" keys"""
    temp = []
    for i in range(len(c_out)):
        if "reliability" in c_out[i] and "country" in c_out[i] and "user" in c_out[i]:
            temp.append(c_out[i])
    return Collection(temp)


def complete_values(c_out):
    """return a new collection that all it's dictionaries have "type" key,
     if it was missing assign it's "type" to "other" """
    temp = c_out.iterable
    for i in range(len(c_out)):
        if "type" not in c_out[i]:
            temp[i]["type"] = "other"
    return Collection(temp)


def get_average_reliability(c_out):
    """return the average reliability for all alerts in Israel"""
    sum = 0
    users = 0
    for i in range(len(c_out)):
        if c_out[i]["country"] == "IL":
            users += 1
            sum += c_out[i]["reliability"]
    return sum / users


def get_top_100_users(collection):
    """ return a collection of the top 100 most active users based on the amount of alerts
   they posted sorted from most popular to least."""

    alerts_list = list(collection.iterable)
    """ [{"user" : "","country": ""},{"user" : "","country": ""}...]"""
    d = dict()  # d= {}
    for alert in alerts_list:  # alert = {"user" :"name"...}
        current_user = alert.get("user")
        if current_user not in d:
            counter = 0
            for a in alerts_list:  # a = {"user" :"name"...}
                if a.get("user") == current_user:
                    # increase user counter, remove duplicate
                    counter += 1
                    del a
            # add (user,counter), counter= 0
            d[current_user] = counter
    d = Collection([dict([("user", user), ("alerts", d[user])]) for user in d])
    d = d.sort(key="alerts", reversed=True).iterable
    d = Collection([x["user"] for x in d][:100])
    return d


def get_top_accident_notifyer(c):
    """
    return the user who posts the most amount of accidents.
    """
    alerts_list = list(c.iterable)
    d = dict()  # d= {}
    for alert in alerts_list:  # alert = {"user" :"name"...}
        current_user = alert.get("user")
        if current_user not in d and alert.get("type") == "accident":
            counter = 0
            for a in alerts_list:  # a = {"user" :"name"...}
                if a.get("user") == current_user:
                    # increase user counter, remove duplicate
                    if a.get("type") == "accident":
                        counter += 1
                    del a

            # add (user,counter), counter= 0
            d[current_user] = counter
    d = Collection([dict([("user", user), ("alerts", d[user])]) for user in d])
    d = d.sort(key="alerts", reversed=True).iterable
    return d[0]["user"]


def get_alert_types_by_country(c):
    """
    return a collection of alert types and their counts by Country.
    """
    # outer dict has: country, data
    # data is collection of dict that has "any type":"occurences"
    # for each alert add to it's country (if exist, if not ,create) data-> to it's type +1 (if exist, if not, create)
    alerts_list = list(c.iterable)
    outer_list = list()
    for alert in alerts_list:  # alert = {"user" :"name"...}
        current_country = alert.get("country")
        current_type = alert.get("type")
        if len(outer_list) == 0:
            new_dict = dict([(current_type, 1)])
            outer_list.append(dict([("country", current_country), ("data", Collection(new_dict))]))
        elif not country_in_list(current_country, outer_list):
            new_dict = dict([(current_type, 1)])
            outer_list.append(dict([("country", current_country), ("data", Collection(new_dict))]))
        else:
            for d in outer_list:
                if d["country"] == current_country:
                    data = d["data"].iterable  # list contain single dict
                    new_dict = dict(data[0])
                    # print(new_list)
                    if current_type in new_dict:
                        new_dict[current_type] += 1
                    else:
                        new_dict.update({current_type: 1})
                    d["data"] = Collection(new_dict)
                    del alert
    return Collection(outer_list)


def country_in_list(country, list1):
    for item in list1:
        if item.get("country") == country:
            return True
    return False
