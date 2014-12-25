def highest_affinity(site_list, user_list, time_list):
  max_affinity = 0
  p_covered = []
  q_covered = []

  for i in range(len(site_list)):

    for j in range(len(site_list)):

      if site_list[i] != site_list[j]:

        if len(p_covered) == 0:
          p_covered.append(site_list[i])
          q_covered.append(site_list[j])
          
        else:
          count = 0

          for l in range(len(p_covered)):
            if ((site_list[i] == p_covered[l] and site_list[j] == q_covered[l]) or (site_list[i] == q_covered[l] and site_list[j] == p_covered[l])):
               count = count * 1
            else:
              count = 1

          if count == 1:
            p_covered.append(site_list[i])
            q_covered.append(site_list[j])

      affinity = 0
      user_covered = []

      if len(p_covered) > 0:
        
        for k in range(len(site_list)):
          for m in range(len(site_list)):
            if p_covered[len(p_covered) - 1] == site_list[k] and q_covered[len(q_covered) - 1] == site_list[m] and user_list[m] == user_list[k] and user_list[k] not in user_covered:
              user_covered.append(user_list[k])
              affinity += 1
        

      if affinity > max_affinity:
        max_affinity = affinity
        Site_P = p_covered[len(p_covered) - 1]
        Site_Q = q_covered[len(q_covered) - 1]

  output = []
  output.append(Site_P)
  output.append(Site_Q)
  output.sort()
  
  return (tuple(output))







