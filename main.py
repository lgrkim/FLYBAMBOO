#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:15:40 2024

@author: laurenkim
"""
import pygame
import os
import sys

os.chdir('/Users/laurenkim/Downloads/gift')

# Now load the image from the images directory within this folder
image_path = os.path.join('images', 'neuron.png')
neuron_image = pygame.image.load(image_path)

# Initialize Pygame
pygame.init()

screen_width, screen_height = 1200, 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Wonderful Life of Timmy the Pajama Cardinalfish")

font_size = 35
font = pygame.font.SysFont("Times New Roman", font_size)


HELLO, WELCOME, INTRO, CRUX, CHOICE, KILLER1, KILLER2, DEFCON1, DEFCON2, COMFORT1, COMFORT2, COMFORT3, COMFORT4, COMFORT5, COMFORT6, HAPPY1, HAPPY2, HAPPY23, PERISH, HAPPY3, HAPPY4, SPICY, HOORAY, END = (
    "HELLO", "WELCOME", "INTRO", "CRUX", "CHOICE", "KILLER1", "KILLER2", "DEFCON1", "DEFCON2",
    "COMFORT1", "COMFORT2", "COMFORT3", "COMFORT4", "COMFORT5", "COMFORT6",
    "HAPPY1", "HAPPY2", "HAPPY23", "PERISH", "HAPPY3", "HAPPY4", "SPICY", "HOORAY", "END"
)
state=HELLO


def load_image(image_name, new_width=screen_width, new_height=screen_height):
    """Load an image from the images directory and scale it to the new width or height while maintaining aspect ratio."""
    try:
        image_path = os.path.join('images', image_name)  # Assuming 'images' folder is in the current working directory
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (new_width, new_height))  # Scale the image to fit the screen
        return image
    except Exception as e:
        print(f"Failed to load and resize image {image_name}: {e}")
        sys.exit(1)  # Exit if image can't be loaded


images = {
    HELLO: load_image('neuron.png'),
    WELCOME: load_image('ocean.png'),
    INTRO: load_image('reef.png'),
    CRUX: load_image('storm.png'),
    CHOICE: load_image('minutemaid.png'),
    KILLER1: load_image('fishle.png'),
    KILLER2: load_image('duckling.png'),
    DEFCON1: load_image('mofusand.png'),
    DEFCON2: load_image('chameleon.png'),
    COMFORT1: load_image('cornicello.png'),
    COMFORT2:load_image('soap.png'),
    COMFORT3: load_image('sunset.png'),
    COMFORT4: load_image('bike.png'),
    COMFORT5: load_image('kitty.png'),
    COMFORT6: load_image('kitty2.png'),
    HAPPY1: load_image('prx.png'),
    HAPPY2: load_image('physics.png'),
    HAPPY23:load_image('ibbot.png'),
    PERISH:load_image('math.png'),
    HAPPY3: load_image('timmy.png'),
    HAPPY4:load_image('meow.png'),
    SPICY: load_image('spicy.png'),
    HOORAY:load_image('heart.png'),
    END: load_image('kitty3.png'),
}

# Text for each state
texts = {
    HELLO:"Welcome to Achyuta's Birthday Gift - a little adventure game I put together as a present for adulthood! This state's background is a visualised OpenAi Microscope neuron from CLIP Resnet 50 - this particular microscope model is something Achyuta finds beautiful and you will continue to find more of his favorite things throughout this game. Follow the instructions on the screen to follow along Achyuta's favorite PEA Science Building fish on an adventure!                                   (PRESS A TO CONTINUE)",
    WELCOME: "Once upon a time, in the tropical waters of Singapore, a little fish named Timmy was born. He hatched out of his lonely little cocoon and saw a watery world above him.                                   (PRESS A TO CONTINUE)",
    INTRO: "Earning the rightful nickname Timmy the Timid, he was naturally very shy; the other colorful baby fish didn't want to play with him and were scared off by Timmy's shadowy dark stripes and red eyes. They chased him around the reef and nipped at his fins. Timmy would dejectedly return home and eat some Szechuan Honey BBQ spare ribs for comfort.                                   (PRESS A TO CONTINUE)",
    CRUX: "Suddenly, one overcast afternoon, a great monsoon swept through Timmy’s reef. The sea creatures were sent into chaos - Japanese cuttlefish (escaped from Osaka) burrowed beneath the sands and Myrtle the Turtle from the New England Aquarium swam away. Even the endangered shrimp felt pain as coral dug into their skin. Timmy desperately searched for cover but all the nooks and crannies were taken.                                    (PRESS A TO CONTINUE)",
    CHOICE: "Timmy then saw an empty Minute Maid lemonade bottle floating about next to him, but noticed that his playground bullies were racing to swim inside too. Does Timmy dash inside the bottle to kill all his bullies? Or, does he apply the Trolley Problem ethical dilemma and choose to rescue more lives than his own?                                  (PRESS Y FOR KILLING BULLIES, N FOR LETTING THEM LIVE)",
    KILLER1: "Timmy squeezed into the lemonade bottle and screwed himself shut while the school of young fish begged to be let inside. Sipping the remains of the sweet beverage (45 g of sugar, Achyuta!!), Timmy watched the storm sweep his tormentors into the void.                                   (PRESS A TO CONTINUE)",
    KILLER2: "Quack! Timmy turns around and is shocked to see a disheveled duckling inside the bottle with him. The lost duckling weeped and said she hailed from the Exeter River. She was a long, long way from home. Does Timmy comfort the duckling or yeet her out the bottle?                                   (PRESS Y FOR COMFORT, N FOR BOTTLE EVICTION)",
    DEFCON1: "Timmy shoved the duckling outside the bottle and accidentally squeezed out the bottle himself. Currents tossed him near the gaping mouth of a kitty dressed as a whale shark, a car called DSKDRIVE, and a metal heart made of silver and gold.                                   (PRESS A TO CONTINUE)",
    DEFCON2: "But then… To his right, Timmy saw the most terrible sight: A GIANT CHAMELEON FROM THE NEW ENGLAND REPTILE EXPO PADDLING HIS WAY!! Timmy saw his brief life flash before his eyes and then succumbed to the chameleon’s evil jaws. (PRESS A TO CONTINUE)",
    COMFORT1: "Timmy gave the duckling a long hug and promised she would be returned to her mom all the way in New Hampshire. The duckling quacked quietly and said she was frightened by two kids sitting on a bridge and staring at her family and duck cannibalism occuring rampant within Cornicello’s. (PRESS A TO CONTINUE)",
    COMFORT2: "Suddenly, the sky turned from gray to light blue. Duckling and Timmy glanced at each other and saw that their bottle was floating on a bar of opium soap from Geneva, Switzerland. Nearby, they saw a couple bars of CERN Toblerone chocolate floating on the river surface. At some point, he saw a paper boat made out of sandwich foil from a Flyby’s Cafe Cubano sandwich.(PRESS A TO CONTINUE)",
    COMFORT3: "Somehow, they’d traveled alllllllllll the way to Hopedale, Massachusetts! As they saw the Amtrak and Boston T training away, Duckling and Timmy thought they were saved! (PRESS A TO CONTINUE)",
    COMFORT4: "As they washed up on the banks of the Charles River, near some rental E-Bikes three Asian high schoolers (after delicious dim sum at Hei La Moon) left behind, a great shadow dominated them. They looked up…(PRESS A TO CONTINUE)",
    COMFORT5: "It was a GIANT KITTY WEARING THE HIGGS BOSON CPU AROUND ITS NECK!!!!! The kitty’s name was Hachimi and it pawed at the duckling and Timmy. Do they jump back into the river or run to MIT Baker House for comfort? (PRESS Y FOR RIVER, N FOR RATS AND RSI KIDS)",
    COMFORT6: "NO OPTION WILL SAVE THEM. kitty is too powerful. The last thing the duckling and Timmy hear is a roaring MEOWWWWWWWWWW. (PRESS A TO CONTINUE)",
    HAPPY1: "Timmy let go of the bottle and floated away into nothingness. He drifted for days on end, hallucinating about beat saber workouts, Valorant ranked games, and red bull boba tea. He floated from October 1, 2023 to August 11, 2024. (PRESS A TO CONTINUE)",
    HAPPY2: "He slept for many months and days until he woke up to the sound of a moving vehicle. He heard Peter Morand, a banana cat screaming, and very sus things related to moon estimations: Timmy the Timid had made it onto the 2024 USIYPT bus for Exeter’s team. Driving back home to Phelps Science Center, he was thrown into an unfamiliar fish tank by a disgruntled James DiCarlo, who had been asked one too many times to play poker. (PRESS A TO CONTINUE)",
    HAPPY23:"As soon as he entered the tank, Timmy felt a twinge of guilt for the children poring over textbooks outside his tank. He saw a great, aging man going by the name Jeff Ibbotson outside his tank. Allured by the mans ability to ignite curiosity in children, Timmy wished to join Ibbot. Does Timmy join the ranks of Math Club, or does he stay in his smol tank? (PRESS I FOR IBBOT, U FOR TANK)",
    PERISH:"Timmy is too eeeeeeeeepy to wake up on Sunday mornings for Math Club, just like a certain birthday boy. He is forced to live beside the Soule Hall soldier for all eternity and is killed by Andrew Kim and Yash Shah. (PRESS A TO CONTINUE)",
    HAPPY3: "Timmy spent his days darting away from the other fish, staring at the Science building leather couches as life went on around him. He saw an old chemistry teacher retire after passing out some fake thermodynamics certificates from Jules Van der Waal. He saw some Indian kid building a beta decay detector using potassium from bananas and yapping about a Puzzle Hunt. The one that always wore a yellow jacket and wore wired headphones. Sometimes there was an Asian girl with him and they’d stare into this tank together, watching him intently. (PRESS A TO CONTINUE)",
    HAPPY4: "One day, as a biology teacher leaned in to feed Timmy nori, the Indian kid took a turn to feed the fish. Evidently, it was his 18th birthday today. Tucked away in his palm, he whipped out some Buldak Spicy 2x Tteokbokki from the Cambridge HMart and some Szechuan Taste Honey BBQ Spareribs. Timmy had a culinary choice before him. (PRESS T FOR TTEOKBOKKI, PRESS S FOR SPARERIBS)",
    SPICY: "Timmy suddenly floated upside down. The spice was too much to bear. He was not Korean or Indian. (PRESS A TO CONTINUE)",
    HOORAY: "Timmy gulped down the cheap Chinese food, and lived happily ever after in his tank. And of course, HAPPY BIRTHDAY ACHYUTA!!!!!!!!!!!! I love you so so SO much and I hope you have the best day! A great person was born 18 years ago today! (if you haven't noticed, the press a to continue is because your name is achyuta :o) (PRESS Q to Quit)",
    END: "Sadly, Timmy's adventure prematurely ends here as he has perished. Press L to restart."
}

def render_text(text, max_width):
    words = text.split(' ')
    lines = []
    current_line = ''
    
    for word in words:
        test_line = f"{current_line} {word}".strip()
        text_surface = font.render(test_line, True, (255, 255, 255))
        if text_surface.get_width() <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    return lines

def display_text(lines, x, y):
    # Calculate the width and height of the text box
    max_line_width = max([font.render(line, True, (255, 255, 255)).get_width() for line in lines])
    box_width = max_line_width + 20  # Add some padding
    box_height = len(lines) * font_size + 20  # Add some padding

    # Calculate the position of the box
    box_x = x - box_width // 2
    box_y = y

    # Draw the background box with a white border
    pygame.draw.rect(screen, (255, 255, 255), (box_x - 2, box_y - 2, box_width + 4, box_height + 4), 2)
    pygame.draw.rect(screen, (50, 50, 50), (box_x, box_y, box_width, box_height))

    # Display the text
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.centerx = x
        text_rect.y = y + i * font_size + 10  # Adjusted y position with padding
        screen.blit(text_surface, text_rect)


# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen
    
    
    screen.blit(images[state], (0, 0))
    
    # Prepare and center text
    text_lines = render_text(texts[state], screen_width - 100)  # 100px margin on the sides
    box_width = screen_width - 100
    box_height = len(text_lines) * font_size + 20  # Add some padding
    box_x = screen_width // 2
    box_y = screen_height // 2 - box_height // 2

    
    pygame.draw.rect(screen, (50, 50, 50), (box_x - box_width // 2, box_y, box_width, box_height))
    
    
    display_text(text_lines, box_x, box_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if state == HELLO and event.key == pygame.K_a:
                state = WELCOME
            elif state == WELCOME and event.key == pygame.K_a:
                state = INTRO
            elif state == INTRO and event.key == pygame.K_a:
                state = CRUX
            elif state == CRUX and event.key == pygame.K_a:
                state = CHOICE
            elif state == CHOICE:
                if event.key == pygame.K_y:
                    state = KILLER1
                elif event.key == pygame.K_n:
                    state = HAPPY1
            elif state == KILLER1 and event.key == pygame.K_a:
                state = KILLER2
            elif state == KILLER2:
                if event.key == pygame.K_y:
                    state = COMFORT1
                elif event.key == pygame.K_n:
                    state = DEFCON1
            elif state == DEFCON1 and event.key == pygame.K_a:
                state = DEFCON2
            elif state == COMFORT1 and event.key == pygame.K_a:
                state = COMFORT2
            elif state == COMFORT2 and event.key == pygame.K_a:
                state = COMFORT3
            elif state == COMFORT3 and event.key == pygame.K_a:
                state = COMFORT4
            elif state == COMFORT4 and event.key == pygame.K_a:
                state = COMFORT5
            elif state == COMFORT5 and event.key == pygame.K_y:
                state = COMFORT6
            elif state == COMFORT5 and event.key == pygame.K_n:
                state = COMFORT6
            elif state == HAPPY1 and event.key == pygame.K_a:
                state = HAPPY2
            elif state == HAPPY2 and event.key == pygame.K_a:
                state = HAPPY23
            elif state == HAPPY23:
                if event.key == pygame.K_i:
                    state = PERISH
                elif event.key == pygame.K_u:
                    state = HAPPY3
            elif state == HAPPY3 and event.key == pygame.K_a:
                state = HAPPY4
            elif state == HAPPY4:
                if event.key == pygame.K_t:
                    state = SPICY
                elif event.key == pygame.K_s:
                    state = HOORAY
            elif state in [DEFCON2, COMFORT6, PERISH,SPICY] and event.key == pygame.K_a:
                state = END  # Assuming each has a similar transition for simplicity.
            elif state == END and event.key == pygame.K_l:
                state = WELCOME
            elif state == HOORAY and event.key == pygame.K_q:
                running = False

    pygame.display.flip()  


pygame.quit()
sys.exit()
