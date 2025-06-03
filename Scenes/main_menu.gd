extends Control

func _ready():
	$CenterContainer/VBoxContainer/Button.pressed.connect(_on_start_game)
	
func _on_start_game():
	get_tree().change_scene_to_file("res://Scenes/GameController.tscn")
