extends Button

signal card_flipped(card: Node)

var word: String = ""
var is_revealed: bool = false
var is_matched: bool = false

@onready var label = $Label

func _ready() -> void:
	label.text = ""
	pressed.connect(_on_pressed)
	
func _on_pressed():
	if not is_revealed and not is_matched:
		reveal()
		card_flipped.emit(self)
	
func reveal():
	is_revealed = true 
	label.text = word
	print(word)
	
func conceal():
	is_revealed = false
	label.text = ""
	
func mark_as_matched():
	is_matched = true
	self.disabled = true 
