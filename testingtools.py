import math

def compare_doubles(a, b):
    return abs(a-b) < 0.0001
    
    
def compare_unsorted_lists(a,b):
    if a == None or b == None:
        return a == b
        
    if len(a) != len(b):
        return False
        
    for i in a:
        if a.count(i) != b.count(i):
            return False
            
    return True
    
def compare_sorted_lists(a,b):
    if a == None or b == None:
        return a == b
        
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != a[b]:
            return False
    return True
    

def bucket_contains_entry(s, bucket):
    for entry in bucket:
        if entry["url"] == s["url"]:
            if abs(entry["score"] - s["score"]) < 0.001 and entry["title"] == s["title"]:
                return True
    return False
    

def compare_search_results(student, expected, k=10, tol=1e-6):
    #exp_sorted = sorted(expected, key=lambda d: d["score"], reverse=True)
    
    #if not correct length, can't be correct
    if len(student) != k:
        return False

    # 2. Determine cutoff score
    cutoff_score = expected[k-1]["score"]

    # 3. Partition into mandatory (> cutoff), tie group (≈ cutoff)
    mandatory = [d for d in expected if d["score"] > cutoff_score + tol]
    tie_group = [d for d in expected if math.isclose(d["score"], cutoff_score, abs_tol=tol)]

    mandatory_urls = {d["url"] for d in mandatory}
    tie_urls = {d["url"] for d in tie_group}

    # 4. Student's top-k
    #stu_topk = student[:k]
    stu_urls = [d["url"] for d in student]

    # 5. Membership check
    if not mandatory_urls.issubset(stu_urls):
        return False
    if len(stu_urls) != k:
        return False
    if not set(stu_urls).issubset(mandatory_urls | tie_urls):
        return False

    # 6. Order check: walk through student list, compare against expected buckets
    # Build expected buckets (sorted by score desc, grouped by tolerance)
    buckets = []
    for d in expected:
        if not buckets or not math.isclose(buckets[-1][0]["score"], d["score"], abs_tol=tol):
            buckets.append([d])
        else:
            buckets[-1].append(d)

    # Now walk student's list and ensure they dont skip buckets or go backwards
    bucket_idx = 0
    #for s in stu_urls:
    for s in student:
        # Find which bucket this student result belongs to
        found = False
        for j in range(0, len(buckets)):
            #if s in buckets[j]:
            if bucket_contains_entry(s, buckets[j]):
                if j < bucket_idx:  # jumped backwards
                    return False
                bucket_idx = j
                found = True
                break
        if not found:
            return False

    return True


    