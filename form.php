

<form action="phpfile.php" method="POST" name="water">
    <div>
        <lable for="Rainfall">Rainfall:</lable>
        <div>
            <input type="number" name="Rainfall" required>
        </div>
    </div>
    <div>
        <lable for="Temperature">Temperature:</lable>
        <div>
            <input type="number" name="Temperature" required>
        </div>
    </div>
    <div>
        <lable for="Humidity">Humidity:</lable>
        <div>
            <input type="number" name="Humidity" required>
        </div>
    </div>
    <div>
        <lable for="Day">Day:</lable>
        <div>
            <input type="number" name="Day" required>
        </div>
    </div>
    
    <button name="prediction">Predict</button>
</form>
