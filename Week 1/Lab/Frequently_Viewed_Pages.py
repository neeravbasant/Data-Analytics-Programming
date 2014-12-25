site_list = ["a.com", "b.com", "a.com", "b.com", "a.com", "c.com"]
user_list = ["andy", "andy", "bob", "bob", "charlie", "charlie"]

max_affinity = 0
p_covered = []
q_covered = []

for i in range(len(site_list)):
  flag = 1
  affinity = 0
  user_covered = []
  for j in range(len(site_list)):
    if site_list[i] != site_list[j]:
      while flag == 1:
        if ((site_list[i] in p_covered and site_list[j] in q_covered) or (site_list[i] in q_covered and site_list[j] in p_covered)) is False:
          p_covered.append(site_list[i])
          q_covered.append(site_list[j])
          flag = 0
        else:
          flag = 0
      for k in range(len(site_list)):
        if p_covered[len(p_covered) - 1] == site_list[j] and q_covered[len(q_covered) - 1] == site_list[k] and user_list[j] == user_list[k] and user_list[j] not in user_covered:
          user_covered.append(user_list[j])
          affinity += 1
  if affinity > max_affinity:
    max_affinity = affinity
    Site_P = p_covered[len(p_covered) - 1]
    Site_Q = q_covered[len(q_covered) - 1]

output = []
output.append(Site_P)
output.append(Site_Q)
output.sort()
print tuple(output)