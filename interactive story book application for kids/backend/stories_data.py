# ─── Story Data for Interactive Story Book ────────────────────
# Each story has: title, theme_color, and lines[]
# Each line has: text, character, animation, duration (ms)

stories = {
    "forest": {
        "title": "The Magic Forest",
        "theme_color": "#1a472a",
        "lines": [
            {
                "text": "Welcome to the Whispering Woods, where every tree has a secret to tell.",
                "character": "owl",
                "animation": "fade-in",
                "duration": 5000
            },
            {
                "text": "Suddenly, Barnaby the Bunny hopped into the clearing with a bright blue map!",
                "character": "bunny",
                "animation": "hop-in",
                "duration": 6000
            },
            {
                "text": "'Look!' Barnaby squeaked. 'I found the way to the Golden Carrot!'",
                "character": "bunny",
                "animation": "wiggle",
                "duration": 5000
            },
            {
                "text": "The magic trees rustled their leaves, pointing the way deeper into the forest.",
                "character": "trees",
                "animation": "rustle",
                "duration": 6000
            },
            {
                "text": "They tiptoed past the sleeping bear and found a river made of starlight.",
                "character": "bunny",
                "animation": "float",
                "duration": 6000
            },
            {
                "text": "At the end of the rainbow river, the Golden Carrot glowed like the sun!",
                "character": "owl",
                "animation": "glow",
                "duration": 5000
            },
            {
                "text": "Barnaby shared the carrot with all his forest friends. The End!",
                "character": "all",
                "animation": "zoom-out",
                "duration": 5000
            }
        ]
    },
    "space": {
        "title": "Galaxy Quest",
        "theme_color": "#0a0a2e",
        "lines": [
            {
                "text": "In the furthest corner of the stars, Commander Starlight prepared for blast-off.",
                "character": "commander",
                "animation": "stars-twinkle",
                "duration": 5000
            },
            {
                "text": "3... 2... 1... LIFT OFF! The Rocket zoomed past the moon!",
                "character": "rocket",
                "animation": "rocket-launch",
                "duration": 7000
            },
            {
                "text": "They met a friendly robot named Beep-Boop who was sitting on a shiny asteroid.",
                "character": "robot",
                "animation": "float",
                "duration": 6000
            },
            {
                "text": "'Want some space-cookies?' asked Beep-Boop with a robotic wink.",
                "character": "robot",
                "animation": "wink",
                "duration": 5000
            },
            {
                "text": "They discovered a planet made entirely of cotton candy clouds!",
                "character": "commander",
                "animation": "bounce",
                "duration": 6000
            },
            {
                "text": "A baby alien waved at them from behind a rainbow nebula.",
                "character": "rocket",
                "animation": "wiggle",
                "duration": 5000
            },
            {
                "text": "Together, they flew into the great unknown of the Milky Way. The End!",
                "character": "rocket",
                "animation": "warp-speed",
                "duration": 6000
            }
        ]
    },
    "ocean": {
        "title": "Deep Sea Discovery",
        "theme_color": "#003b5c",
        "lines": [
            {
                "text": "Deep beneath the waves, Finny the Fish was playing hide-and-seek in the coral.",
                "character": "finny",
                "animation": "bubbles",
                "duration": 5000
            },
            {
                "text": "He found a sparkly treasure chest hidden behind a giant purple jellyfish.",
                "character": "chest",
                "animation": "glow",
                "duration": 6000
            },
            {
                "text": "The jellyfish wiggled happily. 'It's a chest of magic bubbles!' it sang.",
                "character": "jellyfish",
                "animation": "wobble",
                "duration": 6000
            },
            {
                "text": "A seahorse named Swirl joined them for an underwater dance party!",
                "character": "finny",
                "animation": "float",
                "duration": 5000
            },
            {
                "text": "They swam through a tunnel of glowing anemones that tickled their fins.",
                "character": "jellyfish",
                "animation": "wiggle",
                "duration": 6000
            },
            {
                "text": "Finny opened the chest, and the whole ocean started to glow with golden light.",
                "character": "chest",
                "animation": "radiate",
                "duration": 7000
            },
            {
                "text": "What a wonderful day under the sea! The End!",
                "character": "finny",
                "animation": "swirl",
                "duration": 5000
            }
        ]
    },
    "jungle": {
        "title": "Jungle Adventure",
        "theme_color": "#064e3b",
        "lines": [
            {
                "text": "Deep inside the jungle, a curious monkey named Milo loved adventures.",
                "character": "monkey",
                "animation": "swing",
                "duration": 5000
            },
            {
                "text": "He met a wise elephant and a playful parrot sitting on a giant leaf.",
                "character": "elephant",
                "animation": "float",
                "duration": 6000
            },
            {
                "text": "“We are searching for the hidden waterfall!” squawked the parrot.",
                "character": "parrot",
                "animation": "wiggle",
                "duration": 5000
            },
            {
                "text": "They pushed through the thick vines, hearing the sound of drums in the distance.",
                "character": "monkey",
                "animation": "rustle",
                "duration": 6000
            },
            {
                "text": "Finally, they found it—the waterfall made of liquid emeralds!",
                "character": "elephant",
                "animation": "glow",
                "duration": 6000
            },
            {
                "text": "Together, they found a magical jungle treasure hidden behind the water.",
                "character": "monkey",
                "animation": "zoom-in",
                "duration": 5000
            },
            {
                "text": "What a wonderful day in the wild jungle! The End!",
                "character": "monkey",
                "animation": "bounce",
                "duration": 5000
            }
        ]
    },
    "superhero": {
        "title": "The City Hero",
        "theme_color": "#b91c1c",
        "lines": [
            {
                "text": "In a busy city of tall buildings, a young hero discovered a secret power.",
                "character": "hero",
                "animation": "hover",
                "duration": 5000
            },
            {
                "text": "With super speed and strength, he helped people in danger every day.",
                "character": "hero",
                "animation": "dash",
                "duration": 6000
            },
            {
                "text": "One day, a giant robot with glowing red eyes attacked the city center!",
                "character": "robot",
                "animation": "shake",
                "duration": 6000
            },
            {
                "text": "“Not on my watch!” shouted the hero, charging his lightning fist.",
                "character": "hero",
                "animation": "lightning",
                "duration": 5000
            },
            {
                "text": "ZAP! The hero bravely stopped the robot and saved everyone in the city.",
                "character": "hero",
                "animation": "pop",
                "duration": 6000
            },
            {
                "text": "The people cheered for their brave protector under the golden sun.",
                "character": "all",
                "animation": "glow",
                "duration": 5000
            },
            {
                "text": "A hero's work is never done. The End!",
                "character": "hero",
                "animation": "zoom-out",
                "duration": 5000
            }
        ]
    }
}
