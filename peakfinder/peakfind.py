def find_peaks(data_list):
    peaks = []
    if len(data_list) < 2:
        return []
    for i in range(len(data_list)):
        if i == 0:
            if data_list[i] > data_list[i + 1]:
                peaks.append(i)
        elif i == len(data_list) - 1:
            if data_list[i] > data_list[i - 1]:
                peaks.append(i)
        else:
            if data_list[i] > data_list[i - 1] and data_list[i] > data_list[i + 1]:
                peaks.append(i)
    return peaks