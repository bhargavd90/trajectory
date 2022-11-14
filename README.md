# Trajectory Analysis


**Steps to run:**

1) Create a virtual env and install the requirements by running : pip install -r requirements.txt
2) Open a terminal at the project and run : streamlit run main.py
3) This opens an app which contains trajectories of people at each floor


**Created trajectories by:**

1) Ran a single linkage clustering algorithm on the whole data to split it in to levels
2) Found 2 levels with a distance threshold of 50 from a single linkage algorithm
3) Now for each level, Ran a single linkage clustering algorithm to find chains of clusters. Each chain represents a trajectory
4) Assigned user_ids with cluster labels
5) Now plotted the trajectories based on timestamps, used "movingpandas" to plot the trajectories.


**Survey and future work**

1) CNN was used to assign trajectories to predefined categories. It was also used to solve trajectory user linkage (Assign trajectories to users or object generating the trajectory)
2) RNN was used to find the next steps in a trajectory
3) Multiple object trajectory tracking: useful for our use case. [Multiple object trajectory tracking](https://www.researchgate.net/publication/4082162_An_algorithm_for_multiple_object_trajectory_tracking). Uses Markov models to differentiate between different objects (different persons in our trajectories)
