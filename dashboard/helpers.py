def get_barcode_data(width, height, activities, assessments, user):
    data = {'height': height}
    markers = {}
    for activity in activities:
        if activity.activity not in assessments:
            continue
        if activity.user in markers:
            markers[activity.user][activity.activity] = max(activity.value,
                    markers[activity.user].get(activity.activity, 0))
        else:
            markers[activity.user] = {activity.activity: activity.value}


    for marker in markers:
        markers[marker] = sum(markers[marker].values())

    if user in markers:
        data['user'] = markers[user]
        del markers[user]
    else:
        data['user'] = 0
    data['people'] = markers.values()

    # Normalise
    maximum = len(assessments)*100
    data['user'] /= float(maximum)
    data['user'] *= width
    data['user'] = int(data['user'])
    for i in range(len(data['people'])):
        data['people'][i] /= maximum
        data['people'][i] *= width
        data['people'][i] = int(data['people'][i])
    return data
