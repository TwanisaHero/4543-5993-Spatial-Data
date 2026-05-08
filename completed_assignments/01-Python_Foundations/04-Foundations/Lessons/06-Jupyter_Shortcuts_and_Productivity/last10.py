93/3:
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label="sin(x)")
plt.title("Line Plot Example")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.show()
93/4:
# Completed reference solution: cos plot
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label="sin(x)", color="blue")
plt.plot(x, np.cos(x), label="cos(x)", color="orange")
plt.title("sin(x) and cos(x)")
plt.xlabel("x")
plt.ylabel("value")
plt.legend()
plt.grid(True)
plt.show()
93/5:
x = np.random.rand(50)
y = np.random.rand(50)
sizes = 300 * np.random.rand(50)
colors = np.random.rand(50)

plt.scatter(x, y, s=sizes, c=colors, alpha=0.6, cmap='viridis')
plt.title("Scatter Plot Example")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(label="color scale")
plt.show()
93/6:
# Completed reference solution: random scatter
rng = np.random.default_rng(42)
x1, y1 = rng.random(30), rng.random(30)
x2, y2 = rng.random(30), rng.random(30)
plt.scatter(x1, y1, color="teal", label="Group 1")
plt.scatter(x2, y2, color="crimson", label="Group 2")
plt.title("Two Random Point Groups")
plt.legend()
plt.show()
93/7:
categories = ["A", "B", "C", "D"]
values = [5, 7, 3, 8]

plt.bar(categories, values)
plt.title("Bar Plot Example")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()
93/8:
# Completed reference solution: food bar chart
foods = ["Tacos", "Pizza", "Sushi", "Pasta"]
ratings = [9, 8, 10, 7]
plt.bar(foods, ratings, color="slateblue")
plt.title("Favorite Food Ratings")
plt.ylabel("Rating")
plt.show()
93/9:
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin(x)", linestyle="--", color="blue")
plt.plot(x, y2, label="cos(x)", linestyle=":", color="red")
plt.title("Customized Line Plot")
plt.xlabel("x (radians)")
plt.ylabel("value")
plt.legend()
plt.grid(True)
plt.show()
93/10:
# Completed reference solution: customized practice plot
x = np.arange(1, 6)
y = [2, 5, 4, 8, 7]
plt.plot(x, y, marker="o", label="score")
plt.title("Customized Practice Plot")
plt.xlabel("Attempt")
plt.ylabel("Score")
plt.legend()
plt.grid(True)
plt.show()
   1: %history -n 1-5  # Show the first 5 commands in this session
   2:
# Save history to a file
%save my_session.py 1-5
