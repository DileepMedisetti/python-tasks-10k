# ==========================================
# Python Sets - Practice Tasks
# ==========================================

# ==========================================
# Task 1: Student Enrollment Analysis
# ==========================================

python_students = {"Ravi", "Anu", "Sai", "Kiran", "Teja"}
sql_students = {"Sai", "Teja", "Rahul", "Anu", "Priya"}

print("===== Task 1: Student Enrollment Analysis =====")

# 1. Students enrolled in both courses
print("1. Both Courses:", python_students.intersection(sql_students))

# 2. Students enrolled only in Python
print("2. Only Python:", python_students.difference(sql_students))

# 3. Students enrolled only in SQL
print("3. Only SQL:", sql_students.difference(python_students))

# 4. Students enrolled in either course
print("4. All Students:", python_students.union(sql_students))

# 5. Students enrolled in exactly one course
print("5. Exactly One Course:", python_students.symmetric_difference(sql_students))


# ==========================================
# Task 2: Employee Skills Management
# ==========================================

team_a = {"Python", "SQL", "Git", "Docker"}
team_b = {"Java", "SQL", "AWS", "Git"}

print("\n===== Task 2: Employee Skills Management =====")

# 1. Common skills
print("1. Common Skills:", team_a.intersection(team_b))

# 2. Skills only in Team A
print("2. Only Team A:", team_a.difference(team_b))

# 3. Skills only in Team B
print("3. Only Team B:", team_b.difference(team_a))

# 4. All skills
print("4. All Skills:", team_a.union(team_b))

# 5. Add Linux and remove Java
team_a.add("Linux")
team_b.remove("Java")

print("5. Team A After Adding Linux:", team_a)
print("   Team B After Removing Java:", team_b)


# ==========================================
# Task 3: Online Store Customers
# ==========================================

amazon = {"Ravi", "Anu", "Kiran", "Sai", "Teja"}
flipkart = {"Sai", "Teja", "Rahul", "Priya", "Anu"}

print("\n===== Task 3: Online Store Customers =====")

# 1. Customers from both stores
print("1. Both Stores:", amazon.intersection(flipkart))

# 2. Only Amazon
print("2. Only Amazon:", amazon.difference(flipkart))

# 3. Only Flipkart
print("3. Only Flipkart:", flipkart.difference(amazon))

# 4. All unique customers
print("4. All Customers:", amazon.union(flipkart))

# 5. Exactly one store
print("5. Exactly One Store:", amazon.symmetric_difference(flipkart))


# ==========================================
# Task 4: Programming Languages Survey
# ==========================================

batch1 = {"Python", "Java", "C", "SQL"}
batch2 = {"Python", "Java", "React", "JavaScript"}

print("\n===== Task 4: Programming Languages Survey =====")

# 1. Languages known by both batches
print("1. Common Languages:", batch1.intersection(batch2))

# 2. Languages only in Batch 1
print("2. Only Batch 1:", batch1.difference(batch2))

# 3. Languages only in Batch 2
print("3. Only Batch 2:", batch2.difference(batch1))

# 4. Check subset
print("4. Is Batch 1 Subset of Batch 2?:", batch1.issubset(batch2))

# 5. Check superset
print("5. Is Batch 2 Superset of Batch 1?:", batch2.issuperset(batch1))


# ==========================================
# Task 5: Website Visitor Analysis
# ==========================================

day1 = {"user1", "user2", "user3", "user4", "user5"}
day2 = {"user3", "user4", "user5", "user6", "user7"}

print("\n===== Task 5: Website Visitor Analysis =====")

# 1. Returning visitors
print("1. Returning Visitors:", day1.intersection(day2))

# 2. Visitors only on Day 1
print("2. Only Day 1:", day1.difference(day2))

# 3. Visitors only on Day 2
print("3. Only Day 2:", day2.difference(day1))

# 4. All unique visitors
print("4. All Visitors:", day1.union(day2))

# 5. Visitors on exactly one day
print("5. Exactly One Day:", day1.symmetric_difference(day2))