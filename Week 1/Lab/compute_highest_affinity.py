###################################
#    Compute Highest Affinity     #
###################################

def highest_affinity(site_list, user_list, time_list):
    # Creating two empty lists for keeping various pairs of site and their affinity count
    final_site_pair = []
    affinity = []
    user_covered = []

    # Creating nested 'for' loops for traversing through each pair and getting their affinity count
    for i in range(len(site_list)):
        for j in range(len(site_list)):
            if site_list[i] != site_list[j]:
                if user_list[i] == user_list[j]:
                    temp_site_pair = site_list[i] + ":" + site_list[j]
                else:
                    continue

                temp_user = []
                temp_user.append(user_list[i])

                if temp_site_pair not in final_site_pair:
                    final_site_pair.append(temp_site_pair)
                    affinity.append(1)
                    user_covered.append(temp_user)
                else:
                    index = final_site_pair.index(temp_site_pair)
                    if user_list[i] not in user_covered[index]:
                        affinity[index] += 1
                        user_covered[index].extend(temp_user)

    # Finding the pair of site having maximum affinity, sorting them and returning as output
    max_index = affinity.index(max(affinity))
    output = final_site_pair[max_index]
    max_affinity_site_pair = output.split(":")
    max_affinity_site_pair.sort()
    print "The site pair which is visited by maximum number of users is", max_affinity_site_pair
    print "The number of users visiting above mentioned sites is", max(affinity)
    return (tuple(max_affinity_site_pair))