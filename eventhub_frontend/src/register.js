// Import necessary modules and dependencies

// Create an instance of Express
const app = express();

// Set up middleware for parsing JSON data
app.use(express.json());

// Create an array to store registered users
const users = [];

// Register a new user
app.post('/register', async (req, res) => {
    try {
        const { firstName, lastName, username, email, password } = req.body;

        // Check if username or email already exists
        const existingUser = users.find(user => user.username === username || user.email === email);
        if (existingUser) {
            return res.status(400).json({ error: 'Username or email already exists' });
        }

        // Validate email format
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            return res.status(400).json({ error: 'Invalid email address' });
        }

        // Validate password strength
        const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$/;
        if (!passwordRegex.test(password)) {
            return res.status(400).json({ error: 'Password must contain at least 8 characters, including uppercase, lowercase, digits, and symbols' });
        }

        // Generate a unique user ID
        const userId = uuidv4();

        // Hash the password
        const hashedPassword = await bcrypt.hash(password, 10);

        // Save the user to the database
        const user = {
            id: userId,
            firstName,
            lastName,
            username,
            email,
            password: hashedPassword
        };
        users.push(user);

        // Send verification email to the user
        const transporter = nodemailer.createTransport({
            // Configure your email provider here
        });

        const mailOptions = {
            from: 'your-email@example.com',
            to: email,
            subject: 'Account Verification',
            text: 'Please verify your account by clicking the link below: [verification link]'
        };

        transporter.sendMail(mailOptions, (error, info) => {
            if (error) {
                console.log(error);
                return res.status(500).json({ error: 'Failed to send verification email' });
            }
            console.log('Verification email sent:', info.response);
            res.status(200).json({ message: 'User registered successfully. Please check your email for account verification.' });
        });
    } catch (error) {
        console.log(error);
        res.status(500).json({ error: 'An error occurred while registering the user' });
    }
});