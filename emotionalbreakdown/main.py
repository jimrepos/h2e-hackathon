# emotionalbreakdown/main.py
import logging
import argparse
from utils.vocabulary import Vocabulary
from utils.preprocess import Preprocess

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--content', help='Enter the content to be processed here', type=str)
parser.add_argument('-t', '--tests', help='Include this argument to show the tests performed originally', action='store_true')
parser.add_argument('-v', '--verbose', help='Increase output verbosity/show working', action='store_true')
parser.add_argument('-b', '--binary', help='Include this argument to score with +1 or -1 for positive or negative lexicon items respectively (without this argument, defaults to using the prepared lexicon grading set)', action='store_true')
parser.add_argument('-l', '--lexicon', help='Include this argument to print out the lexicon', action='store_true')
parser.add_argument('-d', '--divide', help='Include this argument to divide the overall score by the total number of words', action='store_true')
args = parser.parse_args()

class EmotionalBreakdown():
	
	def process_input(self, content):
		clean_content = Preprocess().reformat_submission(content)

		remaining_content = clean_content

		vocabulary = Vocabulary().get_vocabulary()

		sentiment_score = 0

		for v in vocabulary:
			index = 0
			while index < len(remaining_content):
				index = remaining_content.find(v[0], index)
				if index == -1:
					break
				if args.verbose:
					print(v[0] + ' (' + str(v[1]) + ' points) found at', index)
				if args.binary:
					sentiment_score += 1 if v[1] > 0 else -1
				else:
					sentiment_score += v[1]
				index += len(v[0])
			# set the remaining content to be equal to the old minus the references to 'v' above.
			remaining_content = remaining_content.replace(v[0], '')

		if args.divide:
			sentiment_score = (sentiment_score/len(clean_content.split(' ')))
		else:
			sentiment_score = sentiment_score
		print('Words that remain unaccounted for so assumed neutral:', ', '.join(list(filter(None, remaining_content.split()))))
		verdict = ('Positive' if sentiment_score > 0 else ('Negative' if sentiment_score < 0 else 'Neutral'))
		print(verdict, sentiment_score, '\n')
		#print('sentiment score for "' + str(content) + '" was ' + str(sentiment_score), verdict)


	def show_vocabulary(self):
		print('Vocabulary:', Vocabulary().get_vocabulary(), '\n')


if args.content or args.tests or args.verbose or args.lexicon:

	if args.lexicon:
		EmotionalBreakdown().show_vocabulary()
		print('\n\n')

	if args.verbose:
		print('Training sets (of sorts)...\n\n')
		print('Negative responses (1 star):\n')
		EmotionalBreakdown().process_input('Shocking color from the last 2 i ordered all blue with no other color WASTE of time and money.”')
		EmotionalBreakdown().process_input('You sent me the wrong cartridges Unfortunately I did not relies they were wrong untill I had opened them I sent them back explaining but have not received a response')
		EmotionalBreakdown().process_input('Delivery time ridiculous')
		EmotionalBreakdown().process_input('Bought 2 packs of extended life replacement cartridges (H301XL Tri Colour & H301XL Black - both x 2) and all have resulted in poor print quality. Also 1st Tri Colour cartridge failed (printer errors) after very limited use. Print quality may be OK for draft documents but the blurring and overtyping makes final documents unusable. Have had to change back to genuine HP cartridges!')
		EmotionalBreakdown().process_input('Be warned - these people will keep pestering you to write a review when you buy something from them. They do not seem to understand the concept that when people ignore emails asking for a review, it almost certainly means they are not interested in writing one. This review has been written after the fourth or fifth email from them, asking for a review.')
		EmotionalBreakdown().process_input('To be honest I am not impressed. The colours are distorted and all have a purple tint. None of the printing has been successful with these cartridges I bought two sets I don’t imagine I will use the second lot. Took two pics the first is what I got and the second is what should have appeared. Total waste of money')
		EmotionalBreakdown().process_input('My first purchase went great I still have not received my second I am still being asked about my second purchase and would I recommend them')
		EmotionalBreakdown().process_input('Its rubbish avoid')
		EmotionalBreakdown().process_input('I had been perfectly satisfied until now but the order I placed 12 or so days ago has not arrived. Therefore I have to go with \'very poor\'')
		EmotionalBreakdown().process_input('Can not complain about price as cartridges were half the price of original’s . But sadly the black will not fit, have no problem with the other cartridge’s')
		print('\n\n')

		print('Neutral responses (3 stars):\n')
		EmotionalBreakdown().process_input('After my Canon Pixma MG5750 stopped printing yellow and magenta ink the other week I tried various things to start it going again. The cartridges that I have purchased from you for the last few years have been completely satisfactory. However I have had to buy a new Pixma 5750 and the cost from you was £180 whilst from Currys the price was £49.90 delivered in 2 days. Looking through I came across similar sites to yours selling cartridges at much lower cost for this printer, you will understand that I will be giving this some thought and probably trial purchases.')
		EmotionalBreakdown().process_input('The quality of the printed colours is definitely not like the original HP colours (i.e., the aqua colour appears light green when printed and the lime colour appears dark green when printed). However, the quantity of the ink inside the cartridges is more than I expected and I think it is more than the original ones.')
		EmotionalBreakdown().process_input('Good service but some prices are high')
		EmotionalBreakdown().process_input('There is something wrong with cartridges at first- the copies are very pale with parts missing. after 15 copies all seems normal again. i cant fault your service though')
		EmotionalBreakdown().process_input('As a first time user, I found that Cartridge People offered a prompt and efficient service which was greatly appreciated. The only downside is the quality of the ink cartridges, which frequently \'clog up\' my printer. This clears when I initiate the clean cycle but wastes a lot on ink. Otherwise, okay.')
		EmotionalBreakdown().process_input('Not sure the last Cartridge People black XL cartridge for my Epsom printer was indeed the XL version as labelled and not the standard one as it didn\'t seem to last as long as the previous XL I bought from Cartridge People???')
		EmotionalBreakdown().process_input('Price was good at the date of order, delivery speed acceptable but watch out for being bombarded by requests for reviews - every other day so far')
		EmotionalBreakdown().process_input('Your customer service and delivery time is excellent and one of the best I have experienced. However, the \'compatible\' HP 300 cartridges I purchased did not work. I understand HP have really not made it easy for other cartridges to be used but I wasted a great deal of time reading your trouble-shooting tips, forum advice and YouTube videos. I received genuine HP 300 cartridges from your organisation and they worked immediately, but at a higher price from other retailers.')
		EmotionalBreakdown().process_input('I\'ve used CP on a couple of occasions and I\'m reasonably happy with them. Customer Services are particularly good at resolving issues, but their prices for HP like cartridges have risen dramatically and the cashback site that I\'d used to offset this increase registered no purchase made!')
		EmotionalBreakdown().process_input('I can\'t get any better prices anywhere, but I hope you can go even cheaper on Cartridge People branded cartridges.')
		print('\n\n')

		print('Positive responses (5 stars):\n')
		EmotionalBreakdown().process_input('Very helpful and very quick on delivering to')
		EmotionalBreakdown().process_input('Price really good and arrived by following day. Excllent service')
		EmotionalBreakdown().process_input('Great price and service. Fast delivery.')
		EmotionalBreakdown().process_input('Easy to order, very efficient and prompt delivery, excellent service')
		EmotionalBreakdown().process_input('Great service, prompt delivery good value toner product, I will order again.')
		EmotionalBreakdown().process_input('Always great service and excellent prices.')
		EmotionalBreakdown().process_input('Very prompt, I didn\'t know the post service worked that quickly. Seemed like my ink was being delivered in hours. However, I had previously bought the own label version as opposed to Canon printer branded and my printer didn\'t like it, so there was some hassle getting it to work which wasn\'t worth the future risk of trying it again (lower cost v benefit of saving a few quid).')
		EmotionalBreakdown().process_input('Excellent service - cartridges arrived two days after the order was placed.')
		EmotionalBreakdown().process_input('Excellent service at a reasonable price. Delivered at the forecast time.')
		EmotionalBreakdown().process_input('Fair price, next day delivery, immediate cashback tracked. Recommended for hassle free service.')
		print('\n\n')

	if args.tests:
		print('********************** Test data **************************\n\n')
		print('Expecting Positive...')
		EmotionalBreakdown().process_input('Super quick service. Easy internet site to order on. Recommended.\n')
		print('Expecting Negative...')
		EmotionalBreakdown().process_input('My cartridges arrived promptly. Unfortunately although the correct cartridges my printer jammed as installing. Was unable to rectify this and have replaced the printer. Therefore I have wasted money as the cartridges were never actually used.')
		print('Expecting Positive...')
		EmotionalBreakdown().process_input('excellent service as always!\n')
		print('Expecting Positive...')
		EmotionalBreakdown().process_input('My order delivered promptly. It was exactly what I wanted.')
		print('Expecting Positive...')
		EmotionalBreakdown().process_input('Great prices, excellent quick service and a great free pen arrived with our order')
		print('Expecting Positive...')
		EmotionalBreakdown().process_input('speedy service no complaints happy customer')
		print('Expecting Positive...')
		EmotionalBreakdown().process_input('Very easy to deal with if you have your model numbers handy for the machine you want cartrides for. Efficient,as product came very quickly.Price appealed too.')
		print('Expecting Neutral/Positive...')
		EmotionalBreakdown().process_input('Reasonably quick postage..Price is pretty good..Colours are ok.')
		print('Expecting Positive...')
		EmotionalBreakdown().process_input('Very competitively priced items and easy to order. Kept up to date on dispatch that was quick. The yodel delivery gent was the politest we have received. Very pleased.')
		print('Expecting Negative...')
		EmotionalBreakdown().process_input('Cartridge Save would have been cheaper!')
		print('\n\n')

	if args.content:
		print('User Input: ', args.content, '\nCalculating...\n')
		EmotionalBreakdown().process_input(args.content)

else:
	print('\nNo content generating arguments were entered.\n', 'For help using this script, please use "python3 main.py -h"\n')