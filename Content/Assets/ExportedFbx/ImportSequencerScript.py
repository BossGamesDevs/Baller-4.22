#This script was generated with the addons Blender for UnrealEngine : https://github.com/xavier150/Blender-For-UnrealEngine-Addons
#It will import into Unreal Engine all the assets of type StaticMesh, SkeletalMesh, Animation and Pose
#The script must be used in Unreal Engine Editor with UnrealEnginePython : https://github.com/20tab/UnrealEnginePython
#Use this command : unreal_engine.py_exec(r"C:\Users\myles\Documents\Unreal Projects\Baller 4.22\Content\Assets\ExportedFbx\ImportSequencerScript.py")


def CreateSequencer():
	import os.path
	import time
	import configparser
	import unreal_engine as ue
	from unreal_engine.classes import MovieSceneCameraCutTrack, MovieScene3DTransformSection, MovieScene3DTransformTrack, MovieSceneAudioTrack, CineCameraActor, LevelSequenceFactoryNew
	if ue.ENGINE_MINOR_VERSION >= 20:
		from unreal_engine.structs import FloatRange, FloatRangeBound, MovieSceneObjectBindingID, FrameRate
	else:
		from unreal_engine.structs import FloatRange, FloatRangeBound, MovieSceneObjectBindingID
	from unreal_engine import FTransform, FRotator, FVector, FColor
	from unreal_engine.enums import EMovieSceneObjectBindingSpace
	from unreal_engine.structs import MovieSceneObjectBindingID


	seqPath = r'/Game/ImportedFbx/Sequencer'
	seqName = r'MySequence'
	seqTempName = r'MySequence'+str(time.time())
	mustBeReplace = False
	startFrame = 1
	endFrame = 251
	frameRateDenominator = 1.0
	frameRateNumerator = 24
	secureCrop = 0.0001 #add end crop for avoid section overlay


	def AddSequencerSectionTransformKeysByIniFile(SequencerSection, SectionFileName, FileLoc):
		Config = configparser.ConfigParser()
		Config.read(FileLoc)
		for option in Config.options(SectionFileName):
			frame = float(option)/float(frameRateNumerator) #FrameRate
			list = Config.get(SectionFileName, option)
			list = list.split(',')
			transform = FTransform(FVector(float(list[0]), float(list[1]), float(list[2])), FRotator(float(list[3]), float(list[4]), float(list[5])))
			SequencerSection.sequencer_section_add_key(frame,transform)


	def AddSequencerSectionFloatKeysByIniFile(SequencerSection, SectionFileName, FileLoc):
		Config = configparser.ConfigParser()
		Config.read(FileLoc)
		for option in Config.options(SectionFileName):
			frame = float(option)/float(frameRateNumerator) #FrameRate
			value = float(Config.get(SectionFileName, option))
			SequencerSection.sequencer_section_add_key(frame,value)


	def AddSequencerSectionBoolKeysByIniFile(SequencerSection, SectionFileName, FileLoc):
		Config = configparser.ConfigParser()
		Config.read(FileLoc)
		for option in Config.options(SectionFileName):
			frame = float(option)/float(frameRateNumerator) #FrameRate
			value = Config.getboolean(SectionFileName, option)
			SequencerSection.sequencer_section_add_key(frame,value)


	if ue.find_asset(seqPath+'/'+seqName):
		print("Warning this file already exists")
		factory = LevelSequenceFactoryNew()
		seq = factory.factory_create_new(seqPath+'/'+seqTempName.replace('.',''))
		mustBeReplace = True
	else:
		factory = LevelSequenceFactoryNew()
		seq = factory.factory_create_new(seqPath+'/'+seqName.replace('.',''))
	if seq is None:
		return 'Error /!\ level sequencer factory_create fail' 

	print("Sequencer reference created")
	print(seq)
	ImportedCamera = [] #(CameraName, CameraGuid)
	print("========================= Import started ! =========================")
	
	#Set frame rate
	if ue.ENGINE_MINOR_VERSION >= 20:
		myFFrameRate = FrameRate()
		myFFrameRate.Denominator = frameRateDenominator
		myFFrameRate.Numerator = frameRateNumerator
		seq.MovieScene.DisplayRate = myFFrameRate
	else:
		seq.MovieScene.FixedFrameInterval = frameRateDenominator/frameRateNumerator
	
	#Set playback range
	seq.sequencer_set_playback_range(startFrame/frameRateNumerator, (endFrame-secureCrop)/frameRateNumerator)
	camera_cut_track = seq.sequencer_add_camera_cut_track()
	world = ue.get_editor_world()


	#Import camera cut section
	camera_cut_section = camera_cut_track.sequencer_track_add_section()
	#Not camera found for this section
	camera_cut_section.sequencer_set_section_range(1/frameRateNumerator, (251-secureCrop)/frameRateNumerator)
	if mustBeReplace == True:
		OldSeq = seqPath+'/'+seqName.replace('.','')+'.'+seqName.replace('.','')
		NewSeq = seqPath+'/'+seqTempName.replace('.','')+'.'+seqTempName.replace('.','')
		print(OldSeq)
		print(NewSeq)
		print("LevelSequence'"+OldSeq+"'")
	print('========================= Imports completed ! =========================')
	
	for cam in ImportedCamera:
		print(cam[0])
	
	print('=========================')
	seq.sequencer_changed(True)
	return 'Sequencer created with success !' 
print(CreateSequencer())
