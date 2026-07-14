# W0D0 Brain Signals: Spiking Activity - en Subtitle Transcript

- Source page: https://compneuro.neuromatch.io/tutorials/W0D0_NeuroVideoSeries/student/W0D0_Tutorial5.html
- YouTube: https://youtube.com/watch?v=1nhioy3f9BY
- Caption track: en (manual)

## 01 · 00:00:00.880 - 00:00:29.040

Hello everyone! Welcome to today's session on Neuromatch Academy. I will be a facilitator for today, and today we're talking "Spiking Activity". Okay, so first to cover what we want to... We're first going to need to talk about neurons, because these are the basic units of the nervous system. You know, they underlie everything that the nervous system is able to do. And there's these neurons and their properties that allow action potentials.

## 02 · 00:00:29.600 - 00:00:59.840

We'll talk about the process of action potentials, and how we currently record them right. And then that will then lead us really into being able to discuss about the value, or the role, that these neurons and the spikes (that they generate) create when it comes to communication within the nervous system. Lastly, we can then discuss the strengths and the limitations; because as great as it is that we can record spikes, nothing is perfect in this world. So, we'll talk about what limits it.

## 03 · 00:01:00.960 - 00:01:33.360

Okay, so as I said the neurons form the basic units of the nervous system, and they are what allows communication within the system, and it all happens via electrical signals. Electrical signals getting bounced around from one neuron to the next. And these neuron -- now you can see here you know, a stereotypical image of a neuron -- have "Dendrites" (you know, just collect electrical signals, and bring it in towards the cell body), the "Cell Bodies" (here) also called "Soma"

## 04 · 00:01:33.920 - 00:02:05.360

(and it's the sum of all the activity that comes in from these dendrites that will then trigger the generation of an action potential), here are the base known as the "Axon Hillock", and then the action potential will then be you know propagated along the axon all the way to the "Axon Terminals", where you have these "Synapses". Here neurotransmitters are released, then trigger another electrical signal in an adjacent neuron. Okay, so this would be on the dendrites, ideally,

## 05 · 00:02:05.360 - 00:02:22.080

of an adjacent neuron. Okay, now the first thing to talk about (even before we reach action potentials) are these are the types of potentials called "Graded Potentials". They are basically electrical signals that can be of various intensities. As you can see in the graph here.

## 06 · 00:02:22.640 - 00:02:42.240

So, when the dendrites are (sort of like) collecting information into the soma, what they're doing is summing up (you know) various bits of weighted potentials. And if the sum of all these Graded Potentials exceeds a certain point, it's able to then trigger an action potential. Okay,

## 07 · 00:02:43.920 - 00:03:19.040

so now on to our action potentials (or spike as we like to say). Well, simply we can call them a rapid change in the polarity of the membrane potential. Now there's a number of few words over there, so bear with me right now and I'll try and put that across to you. So, first thing is we know that these cells have a membrane (okay). And this is the extracellular space, and then the intracellular space. I've indicated here that there's a differential distribution of

## 08 · 00:03:19.040 - 00:03:57.840

ions on either side of the membrane. What that means is that, the sum of all the ions you have in the external space is different from how you have in the internal space. So, for example, if you add up all the ions on the external space and subtract it from the ions in the internal space, you end up with a situation where the external space is more positively charged than the internal space. And this differential creates a gradient, and a potential difference, which (when the neuron isn't doing much)

## 09 · 00:03:58.800 - 00:04:29.200

we say it's "-70 millivolts". Now that's great, that's the first thing to make note of. You also need to make note of the fact that there are channels within this membrane which allow selected ions to pass in and out of the cell as they need to. On the outside of the external space, one of the main ions that's there is Sodium (Na), whilst on the inside one of the main ions is Potassium (K). And they almost have equal amounts. So, what I've put here is that,

## 10 · 00:04:29.200 - 00:04:58.000

you know, for the action potential you have the first part which is an influx of Sodium ions. So, Sodium ions coming into the cell and with it bringing a positive charge, so that now the inside of the cell becomes more positively charged, compared to the outside. But shortly after that, you have an influx of Potassium ions -- which is to say, the Potassium ions leave the cell and, take with it, their positive charge. Okay, so what then happens is that the inside becomes

## 11 · 00:04:58.000 - 00:05:21.760

negative again, and this is what is that rapid flip in the polarity, I mentioned. So, allow me to draw another graph similar to what we saw for the graded potentials before. Okay, and on the graph we'll put time in milliseconds over here, and then we'll put our amplitude in millivolts over here.

## 12 · 00:05:22.320 - 00:05:42.160

And we said when the neuron isn't doing much, we have this "-70 millivolts" point, okay, and I had mentioned that you know the graded potentials (when they) exceed a certain point, then you get your action potentials. And that point is typically put at "-55".

## 13 · 00:05:43.520 - 00:06:17.600

Okay, so the reason we say action potentials are "all-or-nothing" (that's indicated here right) is because once you exceed that "-55" point, the consequence is always the same. It's a very stereotypical positive upstroke, all the way to about "+30 millivolts", and then a return back to where we are. So what does that look like? Well, let's take a resting point, it's a membrane potential we're recording. You know, some form of stimulus could have come in. It didn't reach

## 14 · 00:06:17.600 - 00:06:47.040

threshold, so it will come back down, right. The membrane potential comes back down. But, you know, maybe there's a number of different stimuli that came in, and then they built up on each other. And once we hit this threshold point, okay, so that's that threshold. Once we hit this threshold point, you get a stereotypical influx of Sodium, efflux of Potassium, fall below resting potential, and then a return to our resting membrane potential. And there is our action potential. That's why we

## 15 · 00:06:47.040 - 00:07:19.280

say it's all-or-nothing. And the analogy I'd like you to think about is like flushing of toilets. You know, you could start flushing a toilet. Maybe you didn't crank it firm enough, so a little bit of water will go into the chamber and it will just stutter (right), it wouldn't fully flush. But if you were to crank it hard enough, enough water in, then, you know, there a response followed. There will be the water will gush into the pot, there'll be a refill,

## 16 · 00:07:19.280 - 00:07:42.000

and then you can start all over again. It no longer matters how firmly you cranked it, you know, so long as you pass a certain threshold. The sequence or mechanism engages and it's very stereotypical. Another property or a great thing about this analogy is that it also helps us talk about a (sort of, like) refractory period which these action potentials have.

## 17 · 00:07:42.640 - 00:08:10.560

That is to say, from one action potential to the next there always has to be a time delay; just that's from one flush of the toilet, to the next, there will be a time delay (a series or a time difference between them), so that there'll be a maximum number of times you can flush your toilet in a minute. In the same vein, there'll be a maximum number of times you can have an action potential in any given minute. And think about (you know) how that

## 18 · 00:08:11.840 - 00:08:44.080

translates into, for example, how quickly you can move your fingers, right. I can do this slowly and increase the speed but at some point, I will hit a maximum speed, then I can't go anymore. And part of that reason is because it's a maximum frequency that I can send signals to the muscles of my fingers to wriggle them around like that. Okay, so now let's talk about recording, right. So, the first thing is that these... We're recording here spikes from neurons, and the

## 19 · 00:08:44.080 - 00:08:58.720

electrical activities are "very small" in nature, so you can put on a some form of conducting metal or electrode. Some are glass pipettes with the fluid in it, and then a conducting metal.

## 20 · 00:08:59.360 - 00:09:11.440

But they need to be amplified, because these signals are so small. Once it's amplified, then digitized, then some form of acquisition units to help interpret it all together.

## 21 · 00:09:12.400 - 00:09:49.120

So, the spikes that we record, each activity will be (you know) the action potentials are being generated by an individual neuron. You'll be recording activity from an individual neuron. And all the vital information that you need will be based on the frequency and firing pattern. Unlike the graded potentials that have like different intensities and durations, your action potentials have a set intensity right "-70" to "+30", and a set duration which

## 22 · 00:09:49.120 - 00:10:08.320

is about "2" to "4" milliseconds. So, it is within their firing pattern and the frequency of these potentials, that certain pieces of information is coded or hidden in between. And that is where (you know) there's a need to (sort of) sort out the data and make sense of it all.

## 23 · 00:10:09.440 - 00:10:44.320

So, let's talk about these properties: how they relate from the neurons onto the spikes. We've already said that there needs to be some form of threshold reached, right. Now, the "Voltage-gated channels" are the ones that will be allowing the Sodium ions into the cell, and then the Potassium ions out of the cell. So, they are also very important. So, now let's look at how these properties come together to really help us make sense of our spikes. So, we've already said that

## 24 · 00:10:45.120 - 00:11:02.320

some threshold needs to be reached before you get a spike. We've mentioned you have these channels that will need to allow Sodium to come into the cell and Potassium out of cell. And we've also mentioned that neuron will have a maximum sort of firing frequency.

## 25 · 00:11:03.040 - 00:11:29.840

Now, I'm going to throw in another sort of variable into the mix, which is to saying, you can have some channels that don't necessarily open and close in response to a stimuli. They're sort of leaky, right. Like you have a leaky tap which will always allow some amount of water to just drip out. In the same way, you can have these leaky channels that always allow some amount of positive ions to come into the cell. What this means is, over time

## 26 · 00:11:29.840 - 00:11:43.600

they can eventually trigger an action potential, and I'll draw that up for us to look at. So, for example, let's for our graph here again. Okay. And I'm going to draw two separate ones.

## 27 · 00:11:44.800 - 00:12:25.520

So, once again we put time in milliseconds, okay. And amplitude in millivolts. All right. And there's a starting point of "-70", and then a threshold point of "-55". Okay, now if you take the case of these leaky channels, it means that the memory potential could be (you know) down there. But then slowly over time, it will just be depolarizing until it reaches this threshold. Right then you, boom! We kick in with our action potential, right. Now,

## 28 · 00:12:25.520 - 00:12:49.920

imagine if we can then artificially trigger these action potentials. What it means is that we're able to then study the various firing frequencies and firing patterns. So, let's consider (you know) having sort of like action potential, but then we'll draw it on a different scale, okay. And

## 29 · 00:12:51.840 - 00:13:19.840

over here. Where we can then just have a neuron (okay), it's gonna hit threshold, and then you get an action potential, and then you sort of come back, and we stop stimulating it, and it comes down. So, this will be (you know) one spike that's firing in the neuron. Now, if we didn't stimulate it a bit more, we can start seeing different patterns, okay. So, for example, you can have a neuron that has a high activity at the start, and then dies out.

## 30 · 00:13:20.880 - 00:14:00.240

You can have a neuron that (you know) once it hits threshold, it will fire a series at a certain regular frequency, and once you turn it off it goes. Or you can have (you know) various intensities of frequencies, okay. So, something much more rapid. The point is you can have an array of responses from different types of neuron based on what stimulation you're given. And all the properties of the neuron is what it will dictate the sort of responses you'll get. And the last important thing (all right)

## 31 · 00:14:00.240 - 00:14:05.920

that all these electrical properties of the neuron are subject to change. And here's what I mean.

## 32 · 00:14:08.240 - 00:14:26.240

We can then we can relate a neurons activity to an external stimuli (okay), and this can even change in health and disease. So, let's start with relating to external stimuli. In this case, there are certain neurons in the visual system

## 33 · 00:14:27.760 - 00:15:01.520

which are able to trigger their activity based on what we call their "Receptive Fields", what's happening in their receptive fields. And the receptive fields are really just you know a real world location where activity in there corresponds to a specifics of like mapping within the the visual system. Okay, so in this case you can have certain cell types, that within the area of you know external space, where they respond to stimuli.

## 34 · 00:15:02.400 - 00:15:26.160

They respond differently whether the light or the stimuli presented within the center of the receptor field -- as we see in the yellow dot here. Or within the periphery of the receptor films. So, in this type of cell -- that's shown here on the left -- when stimulus or light is shown in the center of its receptor field, it rather increases the spiking activity.

## 35 · 00:15:27.040 - 00:15:58.720

And if you show it to its periphery -- where that's little bit in this periphery and a lot in this periphery -- it rather hinders or reduces its firing activity. And if you can have a cell type that behaves like this, you can then have the opposite, right. One that rather reduces activity if you have light in the center of this receptive field, and then increases activity when you have light in the periphery of its receptive field. But, properties change; they've been almost like

## 36 · 00:15:59.440 - 00:16:31.520

in-built with slightly different properties which means they can behave differently. Also, means that whether it's a healthy neuron, or a diseased state, or you know there's some deficits in it, they can behave differently as well. Like, here's an example of (you know) spikes that are recorded in the auditory system, okay. And in this case (you know) the cells, (they have you know) they can fire a regular low frequency spiking. But then you know if you really

## 37 · 00:16:31.520 - 00:17:01.920

increase the stimulation, you can get a really high frequency firing, like we see here right. Each of these black lines represents a spike. Now, you'd notice that in the diseased states, even if you give it the same sort of stimulation, these spikes look a little bit different. They are not as regular as the normal one. In the same vein, their maximum firing frequency seems to be (you know) not as impressive as the normal state. So, it clearly suggests that in the

## 38 · 00:17:01.920 - 00:17:08.720

diseased state, some functions change, which is then influencing how that neuron behaves.

## 39 · 00:17:10.240 - 00:17:41.280

Now, we can then take this a bit further because one of the things that the nervous system is famous for is how plastic it is, okay. It can change in response to previous activity, and that previous activity can include sort of like effects of drugs that can affect the neurons; you can also include (you know) any manipulations that are made to its properties, some of this could be due to experience think about learning, think about memory, think about the fact that even

## 40 · 00:17:41.280 - 00:18:08.240

if you do not remember that you've seen an item before, if it's shown to you again you can almost you know recognize it. And be like. Wait! Hang on! I think, I've seen this before. Or you get maybe the sense of "déjà vu", right. That's because there are some neurons in there that their properties have changed ever so slightly after your first experience with the item, so that when you experience the item again when you see it or you engage with it again,

## 41 · 00:18:08.240 - 00:18:42.800

it's able to (you know) trigger certain activity to let you know that I've seen this before. Okay, now that's where it gets on the whole next level. Because we can then connect each individual neuron to another one and there are varying properties that subject to change can then also affect the whole network. So, the simplest connection you can get "Forward Excitation", where we say activity on action potential in neuron "A" will then you know cause the release of neurotransmitters and

## 42 · 00:18:42.800 - 00:19:16.720

eventually trigger an action potential in neuron "B". Easy. Now, let's connect it with three. Activity in neuron "A" will trigger activity in neuron "B". However, neuron "B" is an "Inhibitory neuron", what that means is that it rather prevents activity in whichever neuron its connected to. So, in this case we end up with this neuron, rather being silenced. Okay now, let's add some feedback mechanisms into it, where you can have

## 43 · 00:19:18.400 - 00:19:39.920

activity in neuron "A", it will cause activity in neuron "B", which was an inhibitory neuron, right. So the activity in neuron "C" will rather turn to silence neuron "A". So, (you know) it's like well the "A" that started the whole process, sort of, shot himself in the foot. And rather got silenced.

## 44 · 00:19:39.920 - 00:20:13.440

And we can flip that around, where activity in "A", causes activity "B", causes activity in "C" and that just (you know) excites a whole lot more and feeds the cycle. And these networks are the sort of things that you will see in (you know) your body clock, right. You're able to have cycles within the body that change between day and night, or your menstrual cycle (you know) the neurons that will trigger the release of the egg within the ovaries, and so on... Follow a certain

## 45 · 00:20:13.440 - 00:20:49.680

cycle that's based on connecting these different types of neurons and their properties, right. So, if you consider that some of these will have indigenous bursting, so that will be for example, those that have your leaked channels that will (you know) just naturally over time just give you some activity out of nowhere. And then those properties can come together into some of what we call "Central pattern generators". Because, I'm sure by now you're imagining well combinations can be put together and then they can then create you know self-perpetuating systems,

## 46 · 00:20:49.680 - 00:21:22.080

that once you initiate them except sort of pattern of maybe even movements or cares and that's what we see in a person's gait. Once you start walking, everything seems to follow a certain rhythm. All right, let's talk drawbacks. Well, recording spikes it's a bit of a specialist skill, requires a lot of training, but thankfully Pi builder has kits and software to make it easier these days. Next, you're only able to record activity from one cell, so you miss out on

## 47 · 00:21:23.280 - 00:21:38.000

everything else that's happening around that one cell or in its network. Of course, you can record from multiple single cells at the time. Let's say "5" cells, "8" cells, but you're still only getting one activity and you miss out a holistic picture.

## 48 · 00:21:39.120 - 00:22:12.080

The other thing is that each cell is plastic, okay. It's subject to change its properties, and the network that it is in is also subject to change. So, the intervention of you even recording from the cell, it cannot be ruled out whatsoever influence or impact that has on the activity and the properties of the cell. Defaultly, (you know) the longevity of the cells you know cells are notorious for dying out on you, when you need them to stay alive a bit longer. Because bear in mind

## 49 · 00:22:12.080 - 00:22:24.560

you add a stab in the cell by you know sticking an electrode in it or really disrupting its membrane, so some cells may be able to stay viable for a long time other die out quickly.

## 50 · 00:22:25.120 - 00:22:56.640

The quality or the veracity of the recordings that they are giving you know can be questionable, if you are in there for too long and you are changing their properties. And lastly if you get everything right, and everything goes well. The amount of data can be generated is huge, and then there's a need to (sort of) sort it all out make sense of it. And here also there are some automated processes, or even personal programs that people write to help them sort out

## 51 · 00:22:56.640 - 00:23:14.160

all the data. All right, so let's put it all in summary. So, we say neurons are the basic units of the nervous system and the spikes are sort of like the outputs. Now, the properties of the neuron will give rise to various spike patterns -- some of which has been shown on the left here.

## 52 · 00:23:15.280 - 00:23:46.880

Also, the properties are subject to change, you know it's not fixed. And thirdly, the connection with between the neurons can give back to a multitude of possibilities how they relate with one another. But most importantly, what I would like to leave with you, after the session and you should always bear this with you is that if you can pick a certain mechanism or series of connections within networks of neurons, it probably exists.

## 53 · 00:23:46.880 - 00:23:52.640

If it hasn't been shown yet, it's up to you to do so. Okay, thank you for your time!
