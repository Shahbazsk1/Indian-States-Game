# Indian-States-Game
<h2>The user is shown a map of India and prompted to guess the names of 30 Indian states. <br>
  When a correct guess is made, the state name appears at its correct location on the map.</h2>
<h3>Feature	Description</h3>
<ul>
  <li>🗺️ Background Map	Uses a .gif image of India as the game board</li>
  <li>⌨️ User Input	The user types the name of a state via input box</li>
  <li>❌ Exit Option	Typing "Exit" ends the game and creates a CSV file of states not guessed</li>
  <li>🧠 Learning Aid	Missed states are saved in states_to_learn.csv for review</li>
</ul>
<h3>Modules Used:</h3>
<h4>🐢 turtle – Graphics and UI: </h4>
<ul>
  <li><b>turtle.Screen() :</b>	Creates the game window</li>
  <li><b>screen.addshape() :</b> Adds custom .gif image for the map</li>
  <li><b>turtle.shape() :</b> Used to write guessed state names on the map</li>
</ul>
<h4>pandas – Data Handling</h4>
<ul>Feature	Usage:
  <li><b>read_csv() :</b>	Loads state names and their coordinates from 30_states.csv</li>
  <li><b>data[data.state == answer_state] :</b> 	Filters the row for the guessed state</li>
  <li><b>to_list() :</b>	Converts DataFrame column to a list</li>
  <li><b>DataFrame(missing_states) :</b>	Creates a new CSV file of unguessed states</li>
</ul>
<h4>Supporting File: 30_states.csv</h4>
<ul>
  <li>This CSV should include:
    <p>Maharashtra,50,100<br>
    Karnataka,30,80<br>
      .....<br>
  Each row maps a state name to its coordinates on the map image.</p>
  </li>
</ul>
<h4>Example Gameplay</h4>
<ul>
  <li>The game starts and shows a map of India.</li>
  <li>You type "Punjab" — it's correct → label appears on the map.</li>
  <li>You type "Bihar" — it's correct → label appears on the map.</li>
  <li>You type "Exit" → the game ends and saves all remaining states you didn’t guess in a CSV.</li>
</ul>
