import pandas as pd
import random
from datetime import datetime, timedelta

class DummyDataBuilder():
    def __init__(self, row_count=500, output_path=r'C:\Users\Steven Buri\Desktop'):
        self.df = pd.DataFrame(columns=[])
        self.row_count = row_count
        self.output_path = output_path

    def text_column(self, column_name, *column_options):
        
        #establish initial variables
        max_options = len(column_options)

        #generate values in new column
        for i in range (0, self.row_count):
            #select random from column options
            rnd_number = random.randint(0, max_options-1)
            selection = column_options[rnd_number]
            #print(f'random number: {rnd_number}')
            #print(f'resulting selection: {selection} \n')

            #add selection to dataframe
            self.df.at[i, column_name] = selection

    def name_column(self, column_name='Full Name', alternative_first_names=[], alternative_last_names=[], alternative_full_names=[], unique_name_count=10):

        #default first and last names
        possible_first_names = ['Zane', 'Zackary', 'Zack', 'Zachery', 'Zachary', 'Zachariah', 'Young', 'Yong', 'Xavier', 'Wyatt', 'Woodrow', 'Wm', 'Winston', 'Winfred', 'Winford', 'Wilton', 'Wilson', 'Wilmer', 'Willy', 'Willis', 'Willie', 'Willian', 'Williams', 'William', 'Willard', 'Will', 'Wilfredo', 'Wilfred', 'Wilford', 'Wiley', 'Wilburn', 'Wilbur', 'Wilbert', 'Wilber', 'Whitney', 'Weston', 'Wesley', 'Wes', 'Werner', 'Wendell', 'Weldon', 'Wayne', 'Waylon', 'Warren', 'Warner', 'Ward', 'Walton', 'Walter', 'Wally', 'Wallace', 'Walker', 'Waldo', 'Wade', 'Von', 'Vito', 'Virgilio', 'Virgil', 'Vincenzo', 'Vincent', 'Vince', 'Victor', 'Vicente', 'Vernon', 'Vern', 'Vaughn', 'Vance', 'Van', 'Valentine', 'Valentin', 'Val', 'Ulysses', 'Tyson', 'Tyrone', 'Tyron', 'Tyrell', 'Tyree', 'Tyler', 'Ty', 'Tuan', 'Truman', 'Troy', 'Tristan', 'Trinidad', 'Trey', 'Trevor', 'Trenton', 'Trent', 'Travis', 'Tracy', 'Tracey', 'Tory', 'Tony', 'Toney', 'Tommy', 'Tommie', 'Tomas', 'Tom', 'Todd', 'Tod', 'Toby', 'Tobias', 'Titus', 'Timothy', 'Timmy', 'Tim', 'Thurman', 'Thomas', 'Theron', 'Theodore', 'Theo', 'Thanh', 'Thaddeus', 'Thad', 'Terry', 'Terrence', 'Terrell', 'Terrance', 'Terence', 'Teodoro', 'Teddy', 'Ted', 'Taylor', 'Tanner', 'Tad', 'Sylvester', 'Sydney', 'Sung', 'Stuart', 'Stewart', 'Stevie', 'Steven', 'Steve', 'Sterling', 'Stephen', 'Stephan', 'Stefan', 'Stanton', 'Stanley', 'Stanford', 'Stan', 'Stacy', 'Stacey', 'Spencer', 'Sonny', 'Son', 'Solomon', 'Sol', 'Simon', 'Silas', 'Sidney', 'Sid', 'Shon', 'Shirley', 'Sherwood', 'Sherman', 'Shelton', 'Sheldon', 'Shelby', 'Shayne', 'Shawn', 'Shaun', 'Shannon', 'Shane', 'Shad', 'Seymour', 'Seth', 'Sergio', 'Sebastian', 'Sean', 'Scotty', 'Scottie', 'Scott', 'Scot', 'Saul', 'Santos', 'Santo', 'Santiago', 'Sang', 'Sanford', 'Sandy', 'Samuel', 'Samual', 'Sammy', 'Sammie', 'Sam', 'Salvatore', 'Salvador', 'Sal', 'Ryan', 'Rusty', 'Russell', 'Russel', 'Russ', 'Rupert', 'Rufus', 'Rueben', 'Rudy', 'Rudolph', 'Rudolf', 'Rubin', 'Ruben', 'Royce', 'Royal', 'Roy', 'Ross', 'Rosendo', 'Roscoe', 'Rosario', 'Rory', 'Roosevelt', 'Ronny', 'Ronnie', 'Ronald', 'Ron', 'Romeo', 'Roman', 'Rolland', 'Rolf', 'Rolando', 'Roland', 'Roger', 'Rogelio', 'Rodrigo', 'Rodrick', 'Rodolfo', 'Rodney', 'Rodger', 'Roderick', 'Rod', 'Rocky', 'Rocco', 'Robt', 'Robin', 'Roberto', 'Robert', 'Robby', 'Robbie', 'Rob', 'Riley', 'Rigoberto', 'Rico', 'Ricky', 'Rickie', 'Rickey', 'Rick', 'Richie', 'Richard', 'Rich', 'Ricardo', 'Rhett', 'Reynaldo', 'Reyes', 'Rey', 'Rex', 'Reuben', 'Rene', 'Renato', 'Renaldo', 'Reinaldo', 'Reid', 'Reginald', 'Reggie', 'Refugio', 'Reed', 'Raymundo', 'Raymond', 'Raymon', 'Rayford', 'Ray', 'Raul', 'Rashad', 'Raphael', 'Randy', 'Randolph', 'Randell', 'Randall', 'Randal', 'Ramon', 'Ramiro', 'Ralph', 'Raleigh', 'Rafael', 'Quinton', 'Quintin', 'Quinn', 'Quincy', 'Quentin', 'Prince', 'Preston', 'Porter', 'Porfirio', 'Pierre', 'Phillip', 'Philip', 'Phil', 'Peter', 'Pete', 'Perry', 'Percy', 'Pedro', 'Paul', 'Patrick', 'Patricia', 'Pat', 'Pasquale', 'Parker', 'Paris', 'Palmer', 'Pablo', 'Owen', 'Otto', 'Otis', 'Otha', 'Oswaldo', 'Osvaldo', 'Oscar', 'Orville', 'Orval', 'Orlando', 'Oren', 'Omer', 'Omar', 'Ollie', 'Oliver', 'Olin', 'Olen', 'Odis', 'Odell', 'Octavio', 'Numbers', 'Norris', 'Normand', 'Norman', 'Norberto', 'Norbert', 'Nolan', 'Noel', 'Noe', 'Noble', 'Noah', 'Nigel', 'Nicolas', 'Nicky', 'Nickolas', 'Nick', 'Nicholas', 'Newton', 'Neville', 'Nestor', 'Nelson', 'Neil', 'Ned', 'Neal', 'Nathaniel', 'Nathanial', 'Nathanael', 'Nathan', 'Napoleon', 'Myron', 'Myles', 'Murray', 'Moshe', 'Moses', 'Mose', 'Morton', 'Morris', 'Morgan', 'Monty', 'Monte', 'Monroe', 'Moises', 'Mohammed', 'Mohammad', 'Mohamed', 'Modesto', 'Mitchell', 'Mitchel', 'Mitch', 'Miquel', 'Minh', 'Milton', 'Milo', 'Millard', 'Milford', 'Miles', 'Milan', 'Mikel', 'Mike', 'Miguel', 'Mickey', 'Michel', 'Micheal', 'Michale', 'Michal', 'Michael', 'Micah', 'Mervin', 'Merrill', 'Merlin', 'Merle', 'Melvin', 'Mel', 'Mckinley', 'Maynard', 'Maxwell', 'Maximo', 'Max', 'Mauro', 'Mauricio', 'Maurice', 'Matthew', 'Matt', 'Mathew', 'Mason', 'Mary', 'Marvin', 'Marty', 'Martin', 'Marshall', 'Marquis', 'Marlon', 'Marlin', 'Markus', 'Mark', 'Marion', 'Mario', 'Mariano', 'Maria', 'Margarito', 'Marcus', 'Marcos', 'Marco', 'Marcelo', 'Marcellus', 'Marcelino', 'Marcel', 'Marc', 'Manuel', 'Manual', 'Man', 'Malik', 'Malcom', 'Malcolm', 'Major', 'Mack', 'Mac', 'Lynwood', 'Lynn', 'Lyndon', 'Lyman', 'Lyle', 'Luther', 'Lupe', 'Luke', 'Luis', 'Luigi', 'Lucius', 'Lucio', 'Lucien', 'Luciano', 'Lucas', 'Loyd', 'Lowell', 'Louis', 'Louie', 'Lou', 'Lorenzo', 'Loren', 'Lonny', 'Lonnie', 'Long', 'Lon', 'Logan', 'Lloyd', 'Lionel', 'Linwood', 'Lino', 'Lindsey', 'Lindsay', 'Lincoln', 'Lewis', 'Levi', 'Lester', 'Leslie', 'Lesley', 'Les', 'Leroy', 'Leopoldo', 'Leonel', 'Leonardo', 'Leonard', 'Leon', 'Leo', 'Lenny', 'Lenard', 'Len', 'Lemuel', 'Leland', 'Leigh', 'Leif', 'Lee', 'Leandro', 'Lazaro', 'Lawrence', 'Lawerence', 'Laverne', 'Lavern', 'Laurence', 'Lauren', 'Larry', 'Lanny', 'Lane', 'Landon', 'Lance', 'Lamont', 'Lamar', 'Lacy', 'Kyle', 'Kurtis', 'Kurt', 'Kristopher', 'Kristofer', 'Kris', 'Kraig', 'Kory', 'Korey', 'Kirk', 'Kirby', 'Kip', 'King', 'Kim', 'Kieth', 'Kevin', 'Keven', 'Kerry', 'Kermit', 'Kenton', 'Kent', 'Kenny', 'Kennith', 'Kenneth', 'Keneth', 'Kendrick', 'Kendall', 'Ken', 'Kelvin', 'Kelly', 'Kelley', 'Keith', 'Keenan', 'Kasey', 'Karl', 'Kareem', 'Justin', 'Junior', 'Julius', 'Julio', 'Julian', 'Jules', 'Judson', 'Jude', 'Juan', 'Josue', 'Jospeh', 'Josiah', 'Joshua', 'Josh', 'Joseph', 'Josef', 'Jose', 'Jorge', 'Jordon', 'Jordan', 'Jonathon', 'Jonathan', 'Jonas', 'Jonah', 'Jon', 'Johnson', 'Johnny', 'Johnnie', 'Johnie', 'Johnathon', 'Johnathan', 'John', 'Joey', 'Joesph', 'Joel', 'Joe', 'Jody', 'Joaquin', 'Joan', 'Jimmy', 'Jimmie', 'Jim', 'Jewell', 'Jewel', 'Jesus', 'Jessie', 'Jesse', 'Jess', 'Jerry', 'Jerrold', 'Jerrod', 'Jerrell', 'Jeromy', 'Jerome', 'Jerold', 'Jermaine', 'Jeremy', 'Jeremiah', 'Jere', 'Jeramy', 'Jerald', 'Jeffry', 'Jeffrey', 'Jeffery', 'Jefferson', 'Jefferey', 'Jeff', 'Jed', 'Jean', 'Jc', 'Jayson', 'Jay', 'Javier', 'Jasper', 'Jason', 'Jarvis', 'Jarrod', 'Jarrett', 'Jarred', 'Jarod', 'Jared', 'Jan', 'Jamison', 'Jamie', 'Jamey', 'James', 'Jamel', 'Jame', 'Jamar', 'Jamal', 'Jamaal', 'Jake', 'Jaime', 'Jae', 'Jacques', 'Jacob', 'Jackson', 'Jackie', 'Jack', 'Jacinto', 'Ivory', 'Ivan', 'Issac', 'Isreal', 'Israel', 'Ismael', 'Isidro', 'Isiah', 'Isaias', 'Isaiah', 'Isaac', 'Irwin', 'Irving', 'Irvin', 'Ira', 'Ike', 'Ignacio', 'Ian', 'Hyman', 'Hunter', 'Hung', 'Humberto', 'Hugo', 'Hugh', 'Huey', 'Hubert', 'Hoyt', 'Howard', 'Houston', 'Hosea', 'Horacio', 'Horace', 'Hong', 'Homer', 'Hollis', 'Hobert', 'Hiram', 'Hipolito', 'Hilton', 'Hilario', 'Hershel', 'Herschel', 'Herman', 'Heriberto', 'Herbert', 'Herb', 'Henry', 'Hector', 'Heath', 'Haywood', 'Hayden', 'Hassan', 'Harvey', 'Harry', 'Harrison', 'Harris', 'Harold', 'Harley', 'Harland', 'Harlan', 'Hans', 'Hank', 'Hal', 'Hai', 'Guy', 'Gustavo', 'Gus', 'Guillermo', 'Guadalupe', 'Grover', 'Gregory', 'Gregorio', 'Gregg', 'Greg', 'Granville', 'Grant', 'Graig', 'Graham', 'Grady', 'Gordon', 'Gonzalo', 'Glenn', 'Glen', 'Giuseppe', 'Giovanni', 'Gino', 'Gilberto', 'Gilbert', 'Gil', 'Gerry', 'German', 'Gerardo', 'Gerard', 'Geraldo', 'Gerald', 'George', 'Geoffrey', 'Gene', 'Genaro', 'Gaylord', 'Gayle', 'Gavin', 'Gaston', 'Gary', 'Garth', 'Garry', 'Garrett', 'Garret', 'Garland', 'Garfield', 'Galen', 'Gale', 'Gail', 'Gabriel', 'Fritz', 'Freeman', 'Fredrick', 'Fredric', 'Frederick', 'Frederic', 'Freddy', 'Freddie', 'Fred', 'Franklyn', 'Franklin', 'Frankie', 'Frank', 'Francisco', 'Francis', 'Francesco', 'Frances', 'Foster', 'Forrest', 'Forest', 'Floyd', 'Florentino', 'Florencio', 'Fletcher', 'Filiberto', 'Fidel', 'Fernando', 'Fermin', 'Ferdinand', 'Felton', 'Felix', 'Felipe', 'Federico', 'Fausto', 'Faustino', 'Fabian', 'Ezra', 'Ezequiel', 'Ezekiel', 'Everette', 'Everett', 'Evan', 'Eusebio', 'Eugenio', 'Eugene', 'Ethan', 'Esteban', 'Erwin', 'Ervin', 'Errol', 'Ernie', 'Ernesto', 'Ernest', 'Erin', 'Erik', 'Erick', 'Erich', 'Eric', 'Erasmo', 'Enrique', 'Enoch', 'Emory', 'Emmitt', 'Emmett', 'Emmanuel', 'Emilio', 'Emile', 'Emil', 'Emery', 'Emerson', 'Emanuel', 'Elwood', 'Elvis', 'Elvin', 'Elton', 'Elroy', 'Eloy', 'Elmo', 'Elmer', 'Ellsworth', 'Ellis', 'Elliott', 'Elliot', 'Elisha', 'Eliseo', 'Elijah', 'Elias', 'Eli', 'Eldridge', 'Eldon', 'Elden', 'Elbert', 'Efren', 'Efrain', 'Edwin', 'Edwardo', 'Edward', 'Eduardo', 'Edmundo', 'Edmund', 'Edmond', 'Edison', 'Edgardo', 'Edgar', 'Eddy', 'Eddie', 'Ed', 'Earnest', 'Earle', 'Earl', 'Dylan', 'Dwight', 'Dwayne', 'Dwain', 'Dusty', 'Dustin', 'Duncan', 'Dudley', 'Duane', 'Drew', 'Doyle', 'Douglass', 'Douglas', 'Doug', 'Dorsey', 'Dorian', 'Donte', 'Donovan', 'Donny', 'Donnie', 'Donnell', 'Donn', 'Dong', 'Donald', 'Don', 'Dominique', 'Dominick', 'Dominic', 'Domingo', 'Domenic', 'Dirk', 'Dion', 'Dino', 'Dillon', 'Diego', 'Dick', 'Dexter', 'Dewitt', 'Dewey', 'Dewayne', 'Devon', 'Devin', 'Desmond', 'Deshawn', 'Derrick', 'Derick', 'Derek', 'Deon', 'Denver', 'Denny', 'Dennis', 'Denis', 'Demetrius', 'Demarcus', 'Delmer', 'Delmar', 'Delbert', 'Del', 'Dee', 'Deangelo', 'Deandre', 'Dean', 'Davis', 'David', 'Dave', 'Daryl', 'Darwin', 'Darryl', 'Darron', 'Darrin', 'Darrick', 'Darren', 'Darrell', 'Darrel', 'Daron', 'Darnell', 'Darius', 'Dario', 'Darin', 'Daren', 'Darell', 'Dante', 'Danny', 'Dannie', 'Danilo', 'Daniel', 'Danial', 'Dane', 'Dana', 'Dan', 'Damon', 'Damion', 'Damien', 'Damian', 'Dalton', 'Dallas', 'Dale', 'Cyrus', 'Cyril', 'Curtis', 'Curt', 'Cruz', 'Cristopher', 'Cristobal', 'Craig', 'Coy', 'Courtney', 'Cory', 'Cortez', 'Cornell', 'Cornelius', 'Corey', 'Cordell', 'Conrad', 'Connie', 'Columbus', 'Colton', 'Collin', 'Colin', 'Coleman', 'Cole', 'Colby', 'Cody', 'Clyde', 'Clinton', 'Clint', 'Clifton', 'Clifford', 'Cliff', 'Cleveland', 'Cletus', 'Cleo', 'Clemente', 'Clement', 'Clayton', 'Clay', 'Claudio', 'Claude', 'Claud', 'Clark', 'Clarence', 'Clair', 'Chung', 'Chuck', 'Christopher', 'Christoper', 'Christian', 'Chris', 'Chong', 'Chi', 'Chet', 'Chester', 'Chauncey', 'Chase', 'Chas', 'Charlie', 'Charley', 'Charles', 'Chang', 'Chance', 'Chadwick', 'Chad', 'Cesar', 'Cedrick', 'Cedric', 'Cecil', 'Casey', 'Cary', 'Carter', 'Carson', 'Carroll', 'Carrol', 'Carol', 'Carmine', 'Carmen', 'Carmelo', 'Carlton', 'Carlos', 'Carlo', 'Carl', 'Carey', 'Cameron', 'Calvin', 'Caleb', 'Byron', 'Buster', 'Burton', 'Burt', 'Burl', 'Buford', 'Buddy', 'Bud', 'Buck', 'Bryon', 'Bryce', 'Bryant', 'Bryan', 'Bruno', 'Bruce', 'Brooks', 'Broderick', 'Brock', 'Britt', 'Brice', 'Brian', 'Brett', 'Bret', 'Brenton', 'Brent', 'Brendon', 'Brendan', 'Brant', 'Brandon', 'Branden', 'Brain', 'Brady', 'Bradly', 'Bradley', 'Bradford', 'Brad', 'Boyd', 'Boyce', 'Boris', 'Booker', 'Bobby', 'Bobbie', 'Bob', 'Bo', 'Blake', 'Blair', 'Blaine', 'Billy', 'Billie', 'Bill', 'Bertram', 'Bert', 'Berry', 'Bernie', 'Bernardo', 'Bernard', 'Benton', 'Benny', 'Bennie', 'Bennett', 'Benjamin', 'Benito', 'Benedict', 'Ben', 'Beau', 'Basil', 'Barton', 'Bart', 'Barry', 'Barrett', 'Barney', 'Avery', 'Austin', 'Aurelio', 'Augustus', 'Augustine', 'August', 'Aubrey', 'Ashley', 'Asa', 'Arturo', 'Arthur', 'Art', 'Arron', 'Aron', 'Arnulfo', 'Arnoldo', 'Arnold', 'Armando', 'Armand', 'Arlie', 'Arlen', 'Ariel', 'Arden', 'Archie', 'Antwan', 'Antony', 'Antonio', 'Antonia', 'Antone', 'Anton', 'Antoine', 'Antione', 'Anthony', 'Anibal', 'Angelo', 'Angel', 'Andy', 'Andrew', 'Andres', 'Andreas', 'Andrea', 'Andre', 'Anderson', 'Amos', 'Ambrose', 'Amado', 'Alvin', 'Alvaro', 'Alva', 'Alton', 'Alphonso', 'Alphonse', 'Alonzo', 'Alonso', 'Allen', 'Allan', 'Ali', 'Alfredo', 'Alfred', 'Alfonzo', 'Alfonso', 'Alexis', 'Alexander', 'Alex', 'Alejandro', 'Alec', 'Aldo', 'Alden', 'Alberto', 'Albert', 'Alan', 'Al', 'Ahmed', 'Ahmad', 'Agustin', 'Adrian', 'Adolph', 'Adolfo', 'Adan', 'Adam', 'Adalberto', 'Abram', 'Abraham', 'Abel', 'Abe', 'Abdul', 'Aaron']
        possible_last_names = ['Cooke', 'Key', 'Kidd', 'Duarte', 'Lutz', 'Murillo', 'Bolton', 'Cuevas', 'Bright', 'Osborn', 'Shea', 'Barajas', 'Davies', 'Ferrell', 'Forbes', 'Cowan', 'Carney', 'Cooley', 'Vang', 'Gamble', 'Mcknight', 'Chaney', 'Holder', 'Kaiser', 'Haney', 'Riddle', 'Gay', 'Braun', 'Frey', 'Esparza', 'Ritter', 'Ewing', 'Mooney', 'Branch', 'Fritz', 'Mayo', 'Hays', 'Zhang', 'Hinton', 'Mcneil', 'Travis', 'Huerta', 'Archer', 'Benitez', 'Hatfield', 'Downs', 'Andersen', 'Odom', 'Duke', 'Galloway', 'Mercer', 'Rollins', 'Joyce', 'Riggs', 'Terrell', 'Lucero', 'Bird', 'Mcgrath', 'Haas', 'Hendrix', 'Holden', 'Jarvis', 'Zavala', 'Pollard', 'Hooper', 'Baird', 'Whitney', 'Petty', 'Krause', 'Werner', 'Irwin', 'Good', 'Spence', 'Levine', 'Madden', 'Rowland', 'Davila', 'Bray', 'Cherry', 'Daugherty', 'Cantrell', 'Hester', 'Proctor', 'Villegas', 'Mccann', 'Dickson', 'Beltran', 'Mcpherson', 'Dudley', 'Kaufman', 'Compton', 'Stanton', 'Bonilla', 'Mata', 'Maddox', 'Arellano', 'Waller', 'Cordova', 'Booker', 'Montes', 'Costa', 'Novak', 'Schmitt', 'Donaldson', 'Faulkner', 'Ponce', 'Coffey', 'Rasmussen', 'Levy', 'Burch', 'Church', 'Sheppard', 'Sanford', 'Hanna', 'Oconnell', 'Brandt', 'Maynard', 'Stuart', 'Richmond', 'Mccarty', 'Estes', 'Rivers', 'Hayden', 'Nixon', 'Ali', 'Woodward', 'Yu', 'Horne', 'Choi', 'Moyer', 'Chung', 'Haley', 'Benjamin', 'Mullen', 'Rubio', 'Rosario', 'Bernard', 'Krueger', 'Frye', 'Huber', 'Blanchard', 'Sosa', 'Moses', 'Friedman', 'Blevins', 'Best', 'Finley', 'Mckay', 'Ashley', 'Benton', 'Cisneros', 'Farley', 'Crane', 'Lynn', 'Bean', 'Tapia', 'Sampson', 'Clements', 'Dodson', 'Herring', 'Avery', 'Rush', 'Fry', 'Vaughan', 'Gould', 'Meza', 'Valentine', 'Arroyo', 'Potts', 'Shah', 'Bautista', 'Dougherty', 'Landry', 'Duffy', 'Blackburn', 'Raymond', 'Acevedo', 'Harding', 'Hahn', 'Bender', 'Dunlap', 'Mcmahon', 'David', 'Pugh', 'Everett', 'Shepard', 'Bentley', 'Case', 'Ayers', 'Crosby', 'Mcmillan', 'Mays', 'Hurley', 'Pace', 'Pineda', 'Giles', 'Zuniga', 'Mayer', 'Boyle', 'Walls', 'Mcconnell', 'Donovan', 'Michael', 'Villa', 'Peck', 'Mahoney', 'Fitzpatrick', 'Cantu', 'Randolph', 'Frederick', 'Huynh', 'Velazquez', 'Galvan', 'Arias', 'Conrad', 'Spears', 'Noble', 'Hickman', 'Mcfarland', 'Hebert', 'Reilly', 'Pennington', 'Ho', 'Mcintosh', 'House', 'Howe', 'Frost', 'Schaefer', 'Buckley', 'Middleton', 'Glass', 'Bradshaw', 'Mclean', 'Leblanc', 'Livingston', 'Nielsen', 'Weeks', 'Dorsey', 'Morse', 'Mccall', 'Knapp', 'Mora', 'Gillespie', 'Calhoun', 'Ellison', 'Sellers', 'Hull', 'Hardin', 'Lowery', 'Stark', 'Rangel', 'Hendricks', 'Moon', 'Sexton', 'Herman', 'Melendez', 'Rocha', 'Sloan', 'Mcintyre', 'Gentry', 'Durham', 'Gaines', 'Barr', 'Buck', 'Pruitt', 'Bartlett', 'Lozano', 'Kent', 'Browning', 'Blankenship', 'Stout', 'Kerr', 'Odonnell', 'Velez', 'Solomon', 'Meadows', 'Knox', 'Escobar', 'Bullock', 'Whitehead', 'Stein', 'Conway', 'Strong', 'Mckee', 'Berger', 'Leach', 'Orr', 'Barrera', 'Winters', 'Valenzuela', 'Santana', 'Lester', 'Mccullough', 'Yoder', 'Lam', 'Nolan', 'Roach', 'Villanueva', 'Hurst', 'Merritt', 'Prince', 'Mosley', 'Kemp', 'Huang', 'Woodard', 'Jacobson', 'Kline', 'Shannon', 'English', 'Barry', 'Orozco', 'Stafford', 'Mcclain', 'Snow', 'Vance', 'Macdonald', 'Zamora', 'Wu', 'Preston', 'Small', 'Oneal', 'Beasley', 'Barron', 'Clay', 'Eaton', 'Tanner', 'Mercado', 'Blackwell', 'Mcclure', 'Dyer', 'Wilkerson', 'Henson', 'Stephenson', 'Ware', 'Andrade', 'Khan', 'Macias', 'Keith', 'Ibarra', 'Gilmore', 'Beard', 'Hobbs', 'Suarez', 'Koch', 'Johns', 'Humphrey', 'Rich', 'Wiley', 'Mcdowell', 'Walter', 'Liu', 'Hutchinson', 'Golden', 'Baxter', 'Sawyer', 'Russo', 'Marks', 'Salas', 'Brennan', 'Wiggins', 'Savage', 'Pitts', 'Harrell', 'Berg', 'Kane', 'Booth', 'Melton', 'Oneill', 'Parrish', 'Dillon', 'Camacho', 'Delacruz', 'Cline', 'Glenn', 'Grimes', 'Hancock', 'Lin', 'Shields', 'Boyer', 'Roy', 'Huffman', 'Atkins', 'Hensley', 'Callahan', 'Valencia', 'Dalton', 'Heath', 'Villarreal', 'Trevino', 'Garrison', 'Hodge', 'Mathews', 'Vincent', 'Gates', 'Chase', 'Foley', 'Wyatt', 'Bond', 'Dickerson', 'Nash', 'Castaneda', 'Farrell', 'Phelps', 'Christian', 'York', 'Rosales', 'Jefferson', 'Horn', 'Atkinson', 'Sweeney', 'Allison', 'Charles', 'Abbott', 'Boone', 'Bradford', 'Mathis', 'Singleton', 'Bruce', 'Kirk', 'Richard', 'Anthony', 'Bridges', 'Cameron', 'Kirby', 'Wilkinson', 'Skinner', 'Randall', 'Pittman', 'Larsen', 'Franco', 'Combs', 'Roberson', 'Massey', 'Monroe', 'Hood', 'Copeland', 'Huff', 'Houston', 'Conley', 'Davenport', 'Flowers', 'Bass', 'Whitaker', 'Wall', 'Collier', 'Decker', 'Guerra', 'Rivas', 'Greer', 'Gallegos', 'Calderon', 'Poole', 'Clayton', 'Carey', 'Wilcox', 'Serrano', 'Mckenzie', 'Petersen', 'Bryan', 'Summers', 'Holloway', 'Colon', 'Morrow', 'Carson', 'Short', 'Underwood', 'Nicholson', 'Hoover', 'Wilkins', 'Weiss', 'Fuentes', 'Cardenas', 'Meyers', 'Roth', 'Montoya', 'Velasquez', 'Cabrera', 'Ochoa', 'Briggs', 'Olsen', 'Cervantes', 'Li', 'Hess', 'Burnett', 'Cain', 'Shepherd', 'Cochran', 'Patrick', 'Pacheco', 'Lamb', 'Stokes', 'Morton', 'Aguirre', 'Roman', 'Drake', 'Shaffer', 'Trujillo', 'Ballard', 'Brock', 'Lara', 'Pratt', 'Lang', 'Pham', 'Solis', 'Owen', 'Mcbride', 'Marsh', 'Lloyd', 'Lindsey', 'Yates', 'Salinas', 'Robles', 'Hogan', 'Flynn', 'Pope', 'Norton', 'Bauer', 'Leon', 'Mcguire', 'Sparks', 'Conner', 'Moody', 'Gibbs', 'Tyler', 'Clarke', 'Mccormick', 'Kramer', 'French', 'Cobb', 'Buchanan', 'Hartman', 'Floyd', 'Glover', 'Mueller', 'Bowers', 'Logan', 'Patton', 'Casey', 'Harrington', 'Norman', 'Deleon', 'Chan', 'Maxwell', 'Osborne', 'Strickland', 'Waters', 'Frank', 'Parsons', 'Rowe', 'Hampton', 'Schroeder', 'Ayala', 'Mejia', 'Barton', 'Ingram', 'Wise', 'Townsend', 'Carrillo', 'Hammond', 'Mack', 'Tate', 'Saunders', 'Wang', 'Miranda', 'Cannon', 'Hubbard', 'Duran', 'Gallagher', 'Hines', 'Farmer', 'Gill', 'Juarez', 'Hodges', 'Wolf', 'Malone', 'Blake', 'Chang', 'Todd', 'Sherman', 'Avila', 'Campos', 'Fischer', 'Webster', 'Molina', 'Mullins', 'Goodwin', 'Walton', 'Potter', 'Christensen', 'Brady', 'Curry', 'Goodman', 'Adkins', 'Burgess', 'Francis', 'Reese', 'Mcgee', 'Garner', 'Manning', 'Paul', 'Newton', 'Harmon', 'Figueroa', 'Yang', 'Singh', 'Stevenson', 'Rodgers', 'Rojas', 'Mclaughlin', 'Doyle', 'Fitzgerald', 'Moss', 'Navarro', 'Gross', 'Quinn', 'Oconnor', 'Dennis', 'Simon', 'Cross', 'Blair', 'Daniel', 'Chandler', 'Luna', 'Acosta', 'Barber', 'Swanson', 'Hardy', 'Ramsey', 'Cummings', 'Sharp', 'Bowen', 'Griffith', 'Le', 'Cortez', 'Ball', 'Higgins', 'Robbins', 'Love', 'Moran', 'Baldwin', 'Espinoza', 'Klein', 'Reeves', 'Marquez', 'Joseph', 'Dawson', 'Page', 'Mckinney', 'Fletcher', 'Erickson', 'Zimmerman', 'Mann', 'Mccarthy', 'Thornton', 'Bush', 'Padilla', 'Warner', 'Park', 'Miles', 'Haynes', 'Graves', 'Lyons', 'Hale', 'Wolfe', 'Terry', 'Horton', 'Dominguez', 'Neal', 'Benson', 'Steele', 'Schwartz', 'Holt', 'Vazquez', 'Vaughn', 'Norris', 'Barker', 'Watts', 'Mcdaniel', 'Parks', 'Jennings', 'Cohen', 'Sutton', 'Vega', 'Fleming', 'Maldonado', 'Becker', 'Frazier', 'Shelton', 'Gregory', 'Byrd', 'Rhodes', 'Lowe', 'Leonard', 'Craig', 'Nunez', 'Chambers', 'Powers', 'Lambert', 'Santiago', 'Caldwell', 'Barnett', 'Contreras', 'Estrada', 'Wade', 'Ortega', 'Beck', 'Alvarado', 'Bates', 'Stanley', 'Guerrero', 'Keller', 'Hopkins', 'Barrett', 'Sandoval', 'Douglas', 'Rios', 'Pena', 'Valdez', 'Delgado', 'Pearson', 'Curtis', 'Santos', 'Banks', 'Wong', 'Holland', 'Lucas', 'Brewer', 'Newman', 'Schneider', 'Day', 'May', 'Davidson', 'Bowman', 'Fowler', 'Little', 'Walsh', 'Fields', 'Reid', 'Walters', 'Schultz', 'Chen', 'Welch', 'Mccoy', 'Soto', 'Fuller', 'Burton', 'Sims', 'Garrett', 'Weber', 'Hanson', 'Dean', 'Howell', 'Oliver', 'Harvey', 'Montgomery', 'Williamson', 'Jensen', 'Gilbert', 'Mendez', 'Austin', 'Salazar', 'Carr', 'Bishop', 'Franklin', 'Lawson', 'Obrien', 'Jacobs', 'Munoz', 'Morrison', 'Guzman', 'Burke', 'Greene', 'George', 'Harper', 'Carlson', 'Larson', 'Wheeler', 'Watkins', 'Vargas', 'Garza', 'Lawrence', 'Chapman', 'Matthews', 'Willis', 'Richards', 'Silva', 'Aguilar', 'Perkins', 'Carpenter', 'Riley', 'Lane', 'Ray', 'Johnston', 'Andrews', 'Berry', 'Armstrong', 'Duncan', 'Hudson', 'Carroll', 'Bradley', 'Knight', 'Cunningham', 'Elliott', 'Hart', 'Hoffman', 'Castro', 'Hansen', 'Grant', 'Hawkins', 'Peters', 'Spencer', 'Tran', 'Arnold', 'Pierce', 'Dunn', 'Kelley', 'Payne', 'Gardner', 'Stephens', 'Daniels', 'Weaver', 'Fernandez', 'Ryan', 'Medina', 'Herrera', 'Nichols', 'Ferguson', 'Patel', 'Schmidt', 'Moreno', 'Rice', 'Rose', 'Fox', 'Warren', 'Mills', 'Boyd', 'Meyer', 'Stone', 'Holmes', 'Black', 'Robertson', 'Palmer', 'Hunt', 'Dixon', 'Hicks', 'Romero', 'Hunter', 'Wagner', 'Gordon', 'Shaw', 'Mason', 'Porter', 'Jimenez', 'Crawford', 'Simpson', 'Snyder', 'Vasquez', 'Henry', 'Burns', 'Freeman', 'Tucker', 'Washington', 'Webb', 'Olson', 'Castillo', 'Mendoza', 'Woods', 'Alvarez', 'Wells', 'Kennedy', 'Ruiz', 'Harrison', 'Mcdonald', 'Owens', 'Marshall', 'Ford', 'Murray', 'Stevens', 'Ellis', 'Bryant', 'Gibson', 'Chavez', 'Hayes', 'Cole', 'West', 'Griffin', 'Wallace', 'Ramos', 'Alexander', 'Gonzales', 'Kim', 'Graham', 'Hamilton', 'Reynolds', 'Jordan', 'Patterson', 'Simmons', 'Coleman', 'Henderson', 'Fisher', 'Barnes', 'Butler', 'Perry', 'Gutierrez', 'Jenkins', 'Ortiz', 'Russell', 'Sullivan', 'Powell', 'Morales', 'Ross', 'Sanders', 'Foster', 'Long', 'Myers', 'Price', 'Hughes', 'Cruz', 'Reyes', 'James', 'Gray', 'Bennett', 'Brooks', 'Watson', 'Wood', 'Richardson', 'Diaz', 'Cox', 'Ward', 'Howard', 'Kelly', 'Gomez', 'Bell', 'Bailey', 'Reed', 'Cooper', 'Peterson', 'Morgan', 'Rogers', 'Cook', 'Rivera', 'Murphy', 'Nguyen', 'Morris', 'Flores', 'Stewart', 'Edwards', 'Collins', 'Parker', 'Torres', 'Turner', 'Evans', 'Phillips', 'Carter', 'Roberts', 'Mitchell', 'Campbell', 'Ramirez', 'Hill', 'Nelson', 'Adams', 'Baker', 'Green', 'Scott', 'King', 'Wright', 'Sanchez', 'Allen', 'Young', 'Hall', 'Perez', 'Walker', 'Robinson', 'Lewis', 'Clark', 'Harris', 'Gonzalez', 'Lee', 'Lopez', 'White', 'Thompson', 'Jackson', 'Martin', 'Moore', 'Hernandez', 'Thomas', 'Taylor', 'Anderson', 'Martinez', 'Wilson', 'Rodriguez', 'Garcia', 'Davis', 'Miller', 'Jones', 'Brown', 'Williams', 'Johnson', 'Smith']
    
        #generate unique names from possible first and last names, if no full altnerative names given
        if alternative_full_names == []:
            
            #reset firstnames and lastnames if needed
            if alternative_first_names != []:
                possible_first_names = alternative_first_names

            if alternative_last_names != []:
                possible_last_names = alternative_last_names

            unique_names=[]
            while len(unique_names) < unique_name_count:
                #select first name
                max_first_name_options = len(possible_first_names) - 1
                rnd_int_firstname = random.randint(0, max_first_name_options)
                firstname_selection = possible_first_names[rnd_int_firstname]

                #select last name
                max_last_name_options = len(possible_last_names) - 1
                rnd_int_lastname = random.randint(0, max_last_name_options)
                lastname_selection = possible_last_names[rnd_int_lastname]

                #put together full name
                full_name = firstname_selection + " " + lastname_selection

                #add to unique name list if name is not already in list
                
                if full_name not in unique_names:
                    unique_names.append(full_name)
                    #print(f'new unique name: {full_name}')

            #add from unique name list to dataframe
            for i in range(0, self.row_count):
                max_options = len(unique_names)
                rnd_number = random.randint(0, max_options-1)
                selected_name = unique_names[rnd_number]
                self.df.at[i, column_name] = selected_name
        
        #if alternative full names given, use those instead of generating new names from first and last names
        elif alternative_full_names != []:
            for i in range(0, self.row_count):
                max_options = len(alternative_full_names)
                print(max_options)
                print(alternative_full_names)
                rnd_number = random.randint(0, max_options-1)
                selected_name = alternative_full_names[rnd_number]
                self.df.at[i, column_name] = selected_name

    def number_column(self, column_name, min_number, max_number):

        #generate random numbers in target column
        for i in range(0, self.row_count):
            rnd_int = random.randint(min_number, max_number)
            self.df.at[i, column_name] = rnd_int
    
    def date_column_startofmonth(self, column_name, min_year, max_year, min_month=1, max_month=12, conditional_add=False, conditional_column="", conditional_value=""):

        #add days to dataframe
        for i in range(0, self.row_count):
            #obtain selected_day
            day = '01'
            rnd_month = random.randint(min_month, max_month)
            rnd_year = random.randint(min_year, max_year)
            temp_date = str(day) + '/' + str(rnd_month) + '/' + str(rnd_year)
            converted_temp_date = datetime.strptime(temp_date, '%d/%m/%Y')
            selected_date = converted_temp_date
            
            #input selected_day
            if conditional_add == True:
                if self.df.at[i, conditional_column] == conditional_value:
                    self.df.at[i, column_name] = selected_date
            elif conditional_add == False:
                    self.df.at[i, column_name] = selected_date
    
    def date_column_endofmonth(self, column_name, min_year, max_year, min_month=1, max_month=12, conditional_add=False, conditional_column="", conditional_value=""):

        #add days to dataframe
        for i in range(0, self.row_count):
            #obtain selected_day
            rnd_year = random.randint(min_year, max_year)
            rnd_month = random.randint(min_month, max_month)
            rnd_month_modified = int(rnd_month)+1
            if rnd_month_modified == 13:
                rnd_month_modified = 1
                rnd_year += 1
            temp_date = "01" + "/" + str(rnd_month_modified) + "/" + str(rnd_year)
            converted_temp_date = datetime.strptime(temp_date, '%d/%m/%Y')
            selected_date = converted_temp_date - timedelta(days=1)
            
            #input selected_day
            if conditional_add == True:
                if self.df.at[i, conditional_column] == conditional_value:
                    self.df.at[i, column_name] = selected_date
            elif conditional_add == False:
                    self.df.at[i, column_name] = selected_date

    def date_column_anydayinmonth(self, column_name, min_year, max_year, min_month=1, max_month=12, conditional_add=False, conditional_column="", conditional_value=""):

        #add days to dataframe
        for i in range(0, self.row_count):
            #obtain selected_day
            day = random.randint(1,27)
            rnd_month = random.randint(min_month, max_month)
            rnd_year = random.randint(min_year, max_year)
            temp_date = str(day) + '/' + str(rnd_month) + '/' + str(rnd_year)
            converted_temp_date = datetime.strptime(temp_date, '%d/%m/%Y')
            selected_date = converted_temp_date
            
            #input selected_day
            if conditional_add == True:
                if self.df.at[i, conditional_column] == conditional_value:
                    self.df.at[i, column_name] = selected_date
            elif conditional_add == False:
                    self.df.at[i, column_name] = selected_date

    def date_basedoncolumn(self, new_column_name, based_on_column_name, min_days_change, max_days_change, conditional_add=False, conditional_column="", conditional_values=[]):

        #NOTE: based_on_column_name must be a date column, else this will error

        #add new dates to new column based on reference column
        for i in range(0, self.row_count):

            
            #input selected day
            if conditional_add == True:
                if self.df.at[i, conditional_column] in conditional_values:
                    #determine day
                    reference_date = self.df.at[i, based_on_column_name]
                    change_in_days = random.randint(min_days_change, max_days_change)
                    new_date = reference_date + timedelta(days=change_in_days)
                    #print(f'reference date: {reference_date}, \n change_in_days: {change_in_days}, \n new_date: {new_date}')
                    self.df.at[i, new_column_name] = new_date
            elif conditional_add == False:
                #determine day
                reference_date = self.df.at[i, based_on_column_name]
                change_in_days = random.randint(min_days_change, max_days_change)
                new_date = reference_date + timedelta(days=change_in_days)
                #print(f'reference date: {reference_date}, \n change_in_days: {change_in_days}, \n new_date: {new_date}')
                self.df.at[i, new_column_name] = new_date

if __name__=='__main__':

    #psuedocode
    #df_dummy.new_column('column_name', 'column options')

    def test_dummydatabuilder():#test new_column
        dummydata = DummyDataBuilder(row_count=10000)
        dummydata.text_column('test', 'option1', 'option2', 'option3')
        dummydata.text_column('test2', 'a', 'b', '3')
        dummydata.name_column(unique_name_count=10, alternative_full_names=['James Anderson', 'Naveed Patel'])
        dummydata.number_column(column_name='Actuals', min_number=0, max_number=10000000)
        dummydata.date_column_endofmonth(column_name='Actual Close Date', min_year=2019, max_year=2020, conditional_add=True, conditional_column='test', conditional_value='option1')
        print(dummydata.df)
        dummydata.df.to_csv(r'C:\Users\Steven Buri\OneDrive\Z_MyResources\Data Sets\dummydataset.csv', index=False)
    #test_dummydatabuilder()

    def build_salesdashboard():#test new_column
        dummydata = DummyDataBuilder(row_count=1000)
        dummydata.name_column(column_name='Owner', unique_name_count=10)
        dummydata.text_column('Client', 'UTC', 'Southwest', 'PepsiCo', 'Toyota')
        dummydata.text_column('Deal Stage', 'Lost', 'Won', 'Initiated', 'Nearing Close')
        dummydata.name_column(column_name='Client_Names', unique_name_count=10)
        dummydata.number_column(column_name='Potential Value', min_number=0, max_number=10000000)
        dummydata.date_column_endofmonth(column_name='Start Date', min_year=2019, max_year=2020)
        dummydata.date_basedoncolumn(new_column_name='Next Activity Date', based_on_column_name='Start Date', min_days_change=10, max_days_change=50, conditional_add=True, conditional_column='Deal Stage', conditional_values=['Initiated', 'Nearing Close'])
        dummydata.date_basedoncolumn(new_column_name='Close Date', based_on_column_name='Start Date', min_days_change=10, max_days_change=600, conditional_add=True, conditional_column='Deal Stage', conditional_values=['Won', 'Lost'])
        print(dummydata.df)
        dummydata.df.to_csv(r'C:\Users\Steven Buri\OneDrive\Z_MyResources\Data Sets\salesdashboard.csv', index_label='Deal ID')
    build_salesdashboard()