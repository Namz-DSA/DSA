def search(arr, key):
    for a in arr:
        if a == key:
            return True
    return False

print(search([10,20,30,40],30))