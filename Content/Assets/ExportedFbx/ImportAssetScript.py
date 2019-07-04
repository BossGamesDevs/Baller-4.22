def ImportAllAssets():
#This script was generated with the addons Blender for UnrealEngine : https://github.com/xavier150/Blender-For-UnrealEngine-Addons
#This script will import in unreal all camera in target sequencer
#The script must be used in Unreal Engine Editor with UnrealEnginePython : https://github.com/20tab/UnrealEnginePython
#Use this command : unreal_engine.py_exec(r"C:\Users\myles\Documents\Unreal Projects\Baller 4.22\Content\Assets\ExportedFbx\ImportAssetScript.py")


	import os.path
	import configparser
	import ast
	import unreal_engine as ue
	from unreal_engine.classes import PyFbxFactory, AlembicImportFactory, StaticMesh, Skeleton, SkeletalMeshSocket
	from unreal_engine.enums import EFBXImportType, EMaterialSearchLocation, ECollisionTraceFlag
	from unreal_engine.structs import StaticMeshSourceModel, MeshBuildSettings
	from unreal_engine import FVector, FRotator
	
	
	#Prepare var and def
	unrealImportLocation = r'/Game/ImportedFbx'
	ImportedList = []
	ImportFailList = []
	
	def GetOptionByIniFile(FileLoc, OptionName, literal = False):
		Config = configparser.ConfigParser()
		Config.read(FileLoc)
		Options = []
		for option in Config.options(OptionName):
			if (literal == True):
				Options.append(ast.literal_eval(Config.get(OptionName, option)))
			else:
				Options.append(Config.get(OptionName, option))
		return Options
	
	
	#Process import
	print('========================= Import started ! =========================')
	
	
	
	
	'''
	<##############################################################################>
	<#############################	           		#############################>
	<############################	           		 ############################>
	<############################	 StaticMesh tasks	 ############################>
	<############################	           		 ############################>
	<#############################	           		#############################>
	<##############################################################################>
	'''
	
	StaticMesh_TasksList = []
	StaticMesh_PreImportPath = []
	print('========================= Creating StaticMesh tasks... =========================')
	
	def CreateTask_SM_SciFi_Tube_Wiggle():
		################[ Import SciFi_Tube_Wiggle as StaticMesh type ]################
		print('================[ New import task : SciFi_Tube_Wiggle as StaticMesh type ]================')
		FilePath = os.path.join(r'C:\Users\myles\Documents\Unreal Projects\Baller 4.22\Content\Assets\SM_SciFi_Tube_Wiggle.fbx')
		AdditionalParameterLoc = os.path.join(r'C:\Users\myles\Documents\Unreal Projects\Baller 4.22\Content\Assets\SM_SciFi_Tube_Wiggle_AdditionalParameter.ini')
		AssetImportPath = (os.path.join(unrealImportLocation, r'').replace('\\','/')).rstrip('/')
		task = PyFbxFactory()
		task.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_StaticMesh
		task.ImportUI.bImportMaterials = True
		task.ImportUI.bImportTextures = False
		task.ImportUI.bImportAnimations = False
		task.ImportUI.bImportMesh = True
		task.ImportUI.bCreatePhysicsAsset = True
		task.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
		task.ImportUI.StaticMeshImportData.bCombineMeshes = True
		task.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
		task.ImportUI.StaticMeshImportData.bGenerateLightmapUVs = True
		print('================[ import asset : SciFi_Tube_Wiggle ]================')
		try:
			asset = task.factory_import_object(FilePath, AssetImportPath)
		except:
			asset = None
		if asset == None:
			ImportFailList.append('Asset "SciFi_Tube_Wiggle" not found for after inport')
			return
		print('========================= Imports of SciFi_Tube_Wiggle completed ! Post treatment started...	=========================')
		asset.BodySetup.CollisionTraceFlag = ECollisionTraceFlag.CTF_UseDefault 
		lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
		for x, lod in enumerate(lods_to_add):
			pass
			asset.static_mesh_import_lod(lod, x+1)
		print('========================= Post treatment of SciFi_Tube_Wiggle completed !	 =========================')
		asset.save_package()
		asset.post_edit_change()
		ImportedList.append([asset, 'StaticMesh'])
	CreateTask_SM_SciFi_Tube_Wiggle()
	
	
	
	
	def CreateTask_SM_SciFi_Tube_Straight():
		################[ Import SciFi_Tube_Straight as StaticMesh type ]################
		print('================[ New import task : SciFi_Tube_Straight as StaticMesh type ]================')
		FilePath = os.path.join(r'C:\Users\myles\Documents\Unreal Projects\Baller 4.22\Content\Assets\SM_SciFi_Tube_Straight.fbx')
		AdditionalParameterLoc = os.path.join(r'C:\Users\myles\Documents\Unreal Projects\Baller 4.22\Content\Assets\SM_SciFi_Tube_Straight_AdditionalParameter.ini')
		AssetImportPath = (os.path.join(unrealImportLocation, r'').replace('\\','/')).rstrip('/')
		task = PyFbxFactory()
		task.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_StaticMesh
		task.ImportUI.bImportMaterials = True
		task.ImportUI.bImportTextures = False
		task.ImportUI.bImportAnimations = False
		task.ImportUI.bImportMesh = True
		task.ImportUI.bCreatePhysicsAsset = True
		task.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
		task.ImportUI.StaticMeshImportData.bCombineMeshes = True
		task.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
		task.ImportUI.StaticMeshImportData.bGenerateLightmapUVs = True
		print('================[ import asset : SciFi_Tube_Straight ]================')
		try:
			asset = task.factory_import_object(FilePath, AssetImportPath)
		except:
			asset = None
		if asset == None:
			ImportFailList.append('Asset "SciFi_Tube_Straight" not found for after inport')
			return
		print('========================= Imports of SciFi_Tube_Straight completed ! Post treatment started...	=========================')
		asset.BodySetup.CollisionTraceFlag = ECollisionTraceFlag.CTF_UseDefault 
		lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
		for x, lod in enumerate(lods_to_add):
			pass
			asset.static_mesh_import_lod(lod, x+1)
		print('========================= Post treatment of SciFi_Tube_Straight completed !	 =========================')
		asset.save_package()
		asset.post_edit_change()
		ImportedList.append([asset, 'StaticMesh'])
	CreateTask_SM_SciFi_Tube_Straight()
	
	
	
	
	def CreateTask_SM_SciFi_Tube_Hole():
		################[ Import SciFi_Tube_Hole as StaticMesh type ]################
		print('================[ New import task : SciFi_Tube_Hole as StaticMesh type ]================')
		FilePath = os.path.join(r'C:\Users\myles\Documents\Unreal Projects\Baller 4.22\Content\Assets\SM_SciFi_Tube_Hole.fbx')
		AdditionalParameterLoc = os.path.join(r'C:\Users\myles\Documents\Unreal Projects\Baller 4.22\Content\Assets\SM_SciFi_Tube_Hole_AdditionalParameter.ini')
		AssetImportPath = (os.path.join(unrealImportLocation, r'').replace('\\','/')).rstrip('/')
		task = PyFbxFactory()
		task.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_StaticMesh
		task.ImportUI.bImportMaterials = True
		task.ImportUI.bImportTextures = False
		task.ImportUI.bImportAnimations = False
		task.ImportUI.bImportMesh = True
		task.ImportUI.bCreatePhysicsAsset = True
		task.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
		task.ImportUI.StaticMeshImportData.bCombineMeshes = True
		task.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
		task.ImportUI.StaticMeshImportData.bGenerateLightmapUVs = True
		print('================[ import asset : SciFi_Tube_Hole ]================')
		try:
			asset = task.factory_import_object(FilePath, AssetImportPath)
		except:
			asset = None
		if asset == None:
			ImportFailList.append('Asset "SciFi_Tube_Hole" not found for after inport')
			return
		print('========================= Imports of SciFi_Tube_Hole completed ! Post treatment started...	=========================')
		asset.BodySetup.CollisionTraceFlag = ECollisionTraceFlag.CTF_UseDefault 
		lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
		for x, lod in enumerate(lods_to_add):
			pass
			asset.static_mesh_import_lod(lod, x+1)
		print('========================= Post treatment of SciFi_Tube_Hole completed !	 =========================')
		asset.save_package()
		asset.post_edit_change()
		ImportedList.append([asset, 'StaticMesh'])
	CreateTask_SM_SciFi_Tube_Hole()
	
	
	
	
	print('========================= Full import completed !  =========================')
	
	StaticMesh_ImportedList = []
	SkeletalMesh_ImportedList = []
	Alembic_ImportedList = []
	Animation_ImportedList = []
	for asset in ImportedList:
		if asset[1] == 'StaticMesh':
			StaticMesh_ImportedList.append(asset[0])
		elif asset[1] == 'SkeletalMesh':
			SkeletalMesh_ImportedList.append(asset[0])
		elif asset[1] == 'Alembic':
			Alembic_ImportedList.append(asset[0])
		else:
			Animation_ImportedList.append(asset[0])
	
	print('Imported StaticMesh: '+str(len(StaticMesh_ImportedList)))
	print('Imported SkeletalMesh: '+str(len(SkeletalMesh_ImportedList)))
	print('Imported Alembic: '+str(len(Alembic_ImportedList)))
	print('Imported Animation: '+str(len(Animation_ImportedList)))
	print('Import failled: '+str(len(ImportFailList)))
	for error in ImportFailList:
		print(error)
	
	print('=========================')
	if len(ImportFailList) == 0:
		return 'Assets imported with success !' 
	else:
		return 'Some asset(s) could not be imported.' 
	
print(ImportAllAssets())
