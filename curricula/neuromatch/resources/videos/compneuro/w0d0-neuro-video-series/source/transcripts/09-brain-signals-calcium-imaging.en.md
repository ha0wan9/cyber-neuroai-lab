# W0D0 Brain Signals: Calcium Imaging - en Subtitle Transcript

- Source page: https://compneuro.neuromatch.io/tutorials/W0D0_NeuroVideoSeries/student/W0D0_Tutorial9.html
- YouTube: https://youtube.com/watch?v=_eJ-HvecSzU
- Caption track: en (manual)

## 01 · 00:00:00.800 - 00:00:14.000

Hello everyone! My name is Yeka Aponte, and today I'm going to tell you about "Functional imaging of neuronal circuits using genetically encoded Calcium indicators and endomicroscopy systems".

## 02 · 00:00:14.640 - 00:00:55.440

In particular, I'm going to tell you about why and how we use these methods to study and genetically identify cell types and neuronal circuits that drive behaviors essential for survival, such as food intake. So, pioneering studies have identified the hypothalamus as a brain region that regulates survival behaviors, such as feeding, drinking, mating, sleeping, fear, aggression, and nociception. Now, we know that those hypothalamic circuits are composed of a diverse collection of cell types where each performs specific functions has a distinct

## 03 · 00:00:55.440 - 00:01:15.120

set of synaptic connections. And this is just a simple example to show you how rich, in terms of genetically identified cell types, the hypothalamus is. In my opinion, this makes the hypothalamus an ideal circuit to study the neuronal basis of behavior.

## 04 · 00:01:15.680 - 00:01:54.160

Therefore, we needed to develop and use tools to address whether the activity of those cells is sufficient to regulate behavior, but also to establish a correlation between neural activity and the magnitude and dynamics of such behaviors. So, in order to address these questions, we first developed a novel virus based method for cell type specific neuron activation. Briefly, we design a flip-excision or FLEX-switch which allows for very tightly regulated transgene expression,

## 05 · 00:01:54.160 - 00:02:22.400

as in the absence of Cre, the transgene is inverted with respect to the promoter. So, we took advantage of this system to target neurons for optogenetic manipulations. So, we tag the light-activated cation channel, Channelrhodopsin (or ChR2), fused to the fluorescent protein tdTomato for labeling and visualization of our Cre-recombinase dependent viral vector.

## 06 · 00:02:23.120 - 00:02:44.080

Then we stereotaxically injected this virus in the region of interest of Cre transgenic mice. So bear with me for a second please, because I just want you to remember that with this strategy expression of channelrhodopsin will only happen in neurons that express Cre-recombinase.

## 07 · 00:02:45.520 - 00:03:03.840

These schematics show you an example for targeting "agrp neurons" in the "Arcuate nucleus" of the hypothalamus by stereotaxically injecting the Cre-dependent virus into the Arcuate nucleus of agrp-cre transgenic mice, rendering those neurons photoexcitable.

## 08 · 00:03:04.800 - 00:03:25.840

You know now that we can specifically label AGRP, POMC, and other neurons. We can also manipulate their activity in brain slices. But, how to photo-stimulate or photo-inhibit those genetically defined cell populations in the mouse hypothalamus during behavior?

## 09 · 00:03:27.440 - 00:04:07.680

So, we also developed a system that allows to deliver light, deep in the brain. For that, we implant the optical fibers above the region of interest, and delivered light pulses with millisecond precision using a laser. Furthermore, it is also possible to combine traditional electrophysiology methods with optogenetics to record spiking activity from specific cell types during behavior. What you see here is an example of channelrhodopsin-positive neuron, and a silicon probe electrode together with an optical fiber for extracellular recordings

## 10 · 00:04:07.680 - 00:04:52.640

of a spiking activity. These traces show you an example of spikes recorded from hypothalamic neurons. And the idea here is to use optogenetics to identify spiking activity or spiking units corresponding to a genetically defined cell that expresses channelrhodopsin. A major advantage of this strategy is that it allows to measure single action potentials reliably with millisecond precision. However, extracellular electrophysiology is more challenging to perform in a cell type specific fashion and over time. Particularly for excitatory neurons in circuits

## 11 · 00:04:52.640 - 00:05:12.880

with local recurring connections in which photostimulation triggered short latency spikes not only in channelrhodopsin-positive neurons, but also in downstream neurons. And that becomes a challenge when it comes to the identification and analysis of channelrhodopsin-positive neurons.

## 12 · 00:05:12.880 - 00:05:55.120

Also, in order to record from a large number of neurons, high density electrodes such as silicon probes are needed. Now, a major challenge in Systems Neuroscience is recording the activity of multiple neurons in vivo during behavior and over time. Especially, when the neurons or circuits of interest are located deep in the brain. So calcium imaging has some unique advantages compared to traditional extracellular electrophysiology methods. For example, the ability to recall the activity from a large number of neurons and the same neuronal populations across days and weeks,

## 13 · 00:05:55.680 - 00:06:33.920

the ability to map the relative spatial locations of group cells, and the ability to record not only from brain regions in the surface, but also from deep brain structures. So in my lab, we use a combination of viral strategies and fluorescence microendoscopy to establish correlation maps of neural activity patterns that underlie changes in behavior. For that we need to be able to target specific cell types with genetically encoded calcium indicators, image deep brain

## 14 · 00:06:33.920 - 00:06:48.640

structures using GRIN lenses and miniscopes, record from the same neural populations over multiple sessions, and we also need tools for data extraction and analysis. All right,

## 15 · 00:06:50.560 - 00:07:12.880

GCaMPs are fluorescent calcium sensors widely used to image neural activity. For the sake of simplicity, I'm just going to tell you that GCaMP consists of a Green Fluorescent Protein (GFP), the calcium binding protein Calmodulin (CaM), and the Calmodulin interacting M13-peptide.

## 16 · 00:07:13.520 - 00:07:44.080

So when neurons are active, such neuronal activity causes rapid changes in intracellular calcium, and that triggers a conformational change that increases brightness with calcium binding -- as you can see on this schematic. So those changes in fluorescence are used as a proxy for neural activity during behavior. But now how do we target GCaMP to specific neuronal types?

## 17 · 00:07:44.640 - 00:08:17.360

For that we use Cre transgenic mouse lines, and Cre recombinase-dependent viral vectors (typically, Adeno-Associated Viruses) driving the expression of GCaMP6. As I mentioned before, I just want you to remember that with this strategy expression of GCaMP will only happen in neurons that express Cre-recombinase. So, after recovery from viral injections and GRIN lens implantation, we're able to measure the changes in fluorescence as an indicator of neuronal activity.

## 18 · 00:08:18.240 - 00:08:59.520

So, this schematic shows you the expression of GCaMP6 in the lateral hypothalamus, and a GRIN lens chronically implanted and fixed to the skull with dental cement to record those neurons using a single photon miniscope in freely moving mice. Now, we also design a chronically implantable "guide cannula" in collaboration with Doric Lenses which allows for the insertion and removal of GRIN lenses across sessions. By using this approach together with a two-photon system, we are able to visualize GCaMP6-positive neurons in the lateral hypothalamus with sub-cellular

## 19 · 00:08:59.520 - 00:09:32.560

resolution -- as you can see on this image. Furthermore, we were able to visualize the same neurons across days -- as you can see on this image for the lateral hypothalamus and for the striatum. But how do we choose between imaging systems? Well, first we have to consider the experimental question. For example, if you would like to image with sub-cellular resolution, let's say dendrites and axons, a two-photon system will be the option to select. However, for experiments

## 20 · 00:09:32.560 - 00:10:11.200

in freely moving mice a single-photon miniscope or a fiber photometry system are the most popular options. So, let me highlight some of the features of the 3 different systems. With fiber photometry, we can record population dynamics, but it does not provide us with single-cell resolution. An advantage is that we can use it for freely-moving experiments, the system is rather small, and not as expensive as, for example, a two-photon scope. Now with a single-photon miniscope, we get cellular resolution, we can use it for freely moving experiments,

## 21 · 00:10:11.200 - 00:10:39.440

the system is not that large, but a tad more expensive than the fiber photometry system. Last but not least we have the two-photon imaging system: this one allows sub-cellular resolution, three-dimensional images, it is typically used for head-fixed experiments, however, it seems that a freely-moving version is in the making, this type of systems is usually expensive and large.

## 22 · 00:10:40.400 - 00:11:18.160

Therefore, experiments can be designed within the limitations of the selected imaging system, but also keeping in mind the cost and skills required to use any of these systems. For example, the fiber photometry system and single-photon miniscopes are not that hard to use and they are not that expensive. Now in this example, we used a two-photon scope to image the changes in fluorescence from GCaMP6 positive neurons in the lateral hypothalamus during anesthetized and awake state -- as you can see in the video.

## 23 · 00:11:19.280 - 00:12:03.360

Now, every trace is color coded to depict the neurons recorded in the region of interest. So, one more time neuronal activity was measured by the calcium transient changes in fluorescence, also known as "Δf / f". This is represented on these traces. And I would like to highlight, one more time, that calcium imaging does not provide reliable measurement of single action potential as extracellular recordings do. Now, this particular experiment was done on a head-fixed mouse. For this one, we used a single-photon miniscope to image the activity of inhibitory

## 24 · 00:12:03.360 - 00:12:17.360

neurons in the lateral hypothalamus during feeding behaviors in freely moving mouse. In this case, we wanted to check whether these neurons increase or decrease their activity during food intake.

## 25 · 00:12:17.360 - 00:12:37.840

This simple example shows calcium dynamics or changes in fluorescent when a mouse is licking a highly palatable and caloric liquid food. This is depicted here in these gray lines. So this is pretty neat because as you can see time logged events during licking.

## 26 · 00:12:38.880 - 00:12:52.560

So, when it comes to data extraction and data analysis, there are several methods out there. Most of them are free to download, therefore I tremendously encourage you to check this list.

## 27 · 00:12:55.280 - 00:13:11.840

All right, to conclude, I would like to say that these functional imaging methods are really marvelous. Over the past decade, these state-of-the-art methods have contributed to our understanding of how neural circuits and code behavior.

## 28 · 00:13:11.840 - 00:13:37.680

And if you want to learn more details about these methods, I truly recommend our review article, but also my two ultimate favorite review articles on neuron circuits by Luo, Callaway and Svoboda. These articles are really stellar, as they show the progress made for the genetic dissection of neuronal circuits, not only in mice, but also in other model organisms.

## 29 · 00:13:39.360 - 00:13:43.840

With that, I conclude, and thank you all for your kind attention!
