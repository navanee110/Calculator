from direct.showbase.ShowBase import ShowBase
from panda3d.core import Vec3
import random

class TempleRunGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Set up the camera
        self.cam.setPos(0, -20, 5)  # Set camera behind the player
        self.cam.lookAt(0, 0, 0)  # Look at the player's starting position

        # Load the player model (replace with your actual model)
        # For simplicity, we'll use a placeholder for now
        self.player = loader.loadModel("models/smiley")  # Using a default smiley model
        self.player.reparentTo(render)
        self.player.setPos(0, 0, 0)

        # Game variables
        self.speed = 10  # Initial speed of the player
        self.obstacles = []  # List to store obstacles
        self.track_segments = []  # List to store track segments

        # Task for updating the game state
        self.taskMgr.add(self.game_loop, "game_loop")

        # Input handling for player movement (left, right, jump, slide)
        self.accept("arrow_left", self.move_left)
        self.accept("arrow_right", self.move_right)
        self.accept("space", self.jump)

    def game_loop(self, task):
        # Update player position (moving forward)
        self.player.setY(self.player.getY() + self.speed * globalClock.getDt())

        # Generate new track segments and obstacles
        self.generate_track_and_obstacles()

        # Check for collisions (player with obstacles)
        self.check_collisions()

        # Update camera position to follow the player
        self.cam.setY(self.player.getY() - 20)

        return task.cont

    def generate_track_and_obstacles(self):
        # This is where procedural generation would be implemented
        # For now, let's just add a simple track segment and an obstacle
        if len(self.track_segments) < 5:  # Keep a few segments ahead
            new_segment = loader.loadModel("models/cube")  # Placeholder for track segment
            new_segment.reparentTo(render)
            new_segment.setScale(5, 50, 0.1)  # Make it long and flat
            new_segment.setPos(0, len(self.track_segments) * 50, -0.5)
            self.track_segments.append(new_segment)

            # Randomly add an obstacle
            if random.random() < 0.5:
                obstacle = loader.loadModel("models/box")  # Placeholder obstacle
                obstacle.reparentTo(render)
                obstacle.setPos(random.choice([-2, 0, 2]), new_segment.getY() + 20, 0)
                self.obstacles.append(obstacle)

        # Remove old track segments and obstacles
        if self.track_segments and self.track_segments[0].getY() < self.player.getY() - 100:
            self.track_segments[0].removeNode()
            self.track_segments.pop(0)

        if self.obstacles and self.obstacles[0].getY() < self.player.getY() - 100:
            self.obstacles[0].removeNode()
            self.obstacles.pop(0)

    def check_collisions(self):
        # Implement collision detection here
        # For simplicity, we'll just check if the player overlaps with any obstacle
        player_bbox = self.player.getTightBounds()
        for obstacle in self.obstacles:
            obstacle_bbox = obstacle.getTightBounds()
            if player_bbox.intersects(obstacle_bbox):
                print("Game Over!")
                self.userExit()  # Exit the game for now

    def move_left(self):
        self.player.setX(self.player.getX() - 2)

    def move_right(self):
        self.player.setX(self.player.getX() + 2)

    def jump(self):
        # Implement jump mechanics (e.g., vertical movement, then fall back down)
        print("Jump!")


game = TempleRunGame()
game.run()
