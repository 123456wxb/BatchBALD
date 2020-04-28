store = {}
store['args']={'num_inference_samples': 10, 'available_sample_k': 5, 'seed': 67927, 'type': 'AcquisitionFunction.random', 'acquisition_method': 'AcquisitionMethod.independent', 'experiment_description': 'EMNIST_balanced with random acquisition', 'batch_size': 64, 'scoring_batch_size': 512, 'test_batch_size': 512, 'validation_set_size': 16384, 'early_stopping_patience': 3, 'epochs': 40, 'epoch_samples': 20224, 'target_accuracy': 0.85, 'target_num_acquired_samples': 300, 'initial_percentage': 50, 'reduce_percentage': 10, 'min_remaining_percentage': 30, 'min_candidates_per_acquired_item': 100, 'log_interval': 20, 'dataset': 'DatasetEnum.emnist', 'initial_samples': [], 'experiment_task_id': 'emnist_balanced_independent_random_k10_b5_67927', 'experiments_laaos': './experiment_configs/emnist_random/configs.py', 'no_cuda': False, 'quickquick': False, 'initial_samples_per_class': 2}
store['cmdline']=['./src/ignite_mnist.py', '--experiment_task_id=emnist_balanced_independent_random_k10_b5_67927', '--experiments_laaos=./experiment_configs/emnist_random/configs.py']
store['iterations']=[]
store['initial_samples']=[]
store['iterations'].append({'num_epochs': 0, 'test_metrics': {'accuracy': 0.01898936170212766, 'nll': 3.866648737538368}, 'chosen_samples': [99997, 3071, 70929, 95845, 72613], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 22.828086820999943, 'batch_acquisition_elapsed_time': 0.014279005000048528})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.05882978723404255, 'nll': 57.23274244369851}, 'chosen_samples': [42073, 48479, 11663, 30857, 78489], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.64482551800006, 'batch_acquisition_elapsed_time': 0.003012230999956955})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.08909574468085106, 'nll': 51.815406212819376}, 'chosen_samples': [95445, 39838, 5696, 107558, 112775], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.55612721300008, 'batch_acquisition_elapsed_time': 0.0030844299999444047})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.09186170212765958, 'nll': 32.0578775202055}, 'chosen_samples': [72836, 15187, 1402, 76509, 94281], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 76.9744999080001, 'batch_acquisition_elapsed_time': 0.0029896250000547298})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.10888297872340426, 'nll': 30.35059553082826}, 'chosen_samples': [6823, 97125, 41107, 79171, 83888], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 76.50458605999995, 'batch_acquisition_elapsed_time': 0.00346975399997973})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.1576595744680851, 'nll': 35.97518342726915}, 'chosen_samples': [41241, 16563, 57250, 39068, 30091], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.57839488500008, 'batch_acquisition_elapsed_time': 0.0027007450000837707})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.14856382978723404, 'nll': 32.741499462986255}, 'chosen_samples': [58094, 52517, 43611, 106701, 90142], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 49.44179643200005, 'batch_acquisition_elapsed_time': 0.0029669299999568466})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.1753191489361702, 'nll': 30.082707606585092}, 'chosen_samples': [74916, 58399, 94951, 45965, 23044], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 47.76494759000002, 'batch_acquisition_elapsed_time': 0.0028225030000612605})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.17547872340425533, 'nll': 28.052820952367266}, 'chosen_samples': [41912, 39854, 105126, 39249, 35624], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 56.982097504999956, 'batch_acquisition_elapsed_time': 0.0027120889999423525})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.2026595744680851, 'nll': 25.962388740185737}, 'chosen_samples': [78441, 45727, 17174, 42063, 61739], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 39.802842257000066, 'batch_acquisition_elapsed_time': 0.002740219999850524})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.19287234042553192, 'nll': 24.317424426777567}, 'chosen_samples': [38751, 94517, 13193, 4907, 22093], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 50.372927655999774, 'batch_acquisition_elapsed_time': 0.003041125000208922})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.2126063829787234, 'nll': 19.341309689713285}, 'chosen_samples': [54858, 78222, 21357, 53084, 51541], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 58.64828093400001, 'batch_acquisition_elapsed_time': 0.0027994199999739067})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.23632978723404255, 'nll': 19.73912704432835}, 'chosen_samples': [83644, 55331, 57477, 59343, 17095], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 67.75821872200004, 'batch_acquisition_elapsed_time': 0.002910023000140427})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.2422340425531915, 'nll': 16.232421387110616}, 'chosen_samples': [82475, 21574, 75137, 75059, 23586], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 39.5257307280001, 'batch_acquisition_elapsed_time': 0.0026490699999612843})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.24973404255319148, 'nll': 17.375516469039823}, 'chosen_samples': [14231, 16406, 1274, 42211, 65673], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.624664203000066, 'batch_acquisition_elapsed_time': 0.0030782900000758673})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.25542553191489364, 'nll': 16.41958191687249}, 'chosen_samples': [23772, 38031, 3810, 44383, 70098], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 39.97424965799996, 'batch_acquisition_elapsed_time': 0.0027587310000853904})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.2645212765957447, 'nll': 13.634277899091547}, 'chosen_samples': [47645, 77568, 25723, 36870, 99107], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 39.40002400499998, 'batch_acquisition_elapsed_time': 0.002977463999968677})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.2646276595744681, 'nll': 14.208590627490208}, 'chosen_samples': [58863, 50434, 18050, 95913, 4799], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 39.25597925299985, 'batch_acquisition_elapsed_time': 0.002596646000029068})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.27239361702127657, 'nll': 13.19905410453487}, 'chosen_samples': [69144, 7794, 31526, 95549, 29484], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 41.21715931299991, 'batch_acquisition_elapsed_time': 0.0030052459999296843})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.2799468085106383, 'nll': 13.6812373341119}, 'chosen_samples': [98756, 16660, 91941, 79029, 110201], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 39.00135451599999, 'batch_acquisition_elapsed_time': 0.002643728999828454})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.2875, 'nll': 13.813640924316768}, 'chosen_samples': [69047, 28700, 37541, 72221, 7527], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.7424173779998, 'batch_acquisition_elapsed_time': 0.0030079410000780626})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.2945744680851064, 'nll': 12.852410899949199}, 'chosen_samples': [98395, 66288, 59828, 16744, 11368], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.629406892999896, 'batch_acquisition_elapsed_time': 0.002763415999879726})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.3002127659574468, 'nll': 13.263007914392873}, 'chosen_samples': [109798, 85893, 38475, 70276, 94501], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 50.012284333000025, 'batch_acquisition_elapsed_time': 0.002696302000003925})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.31398936170212766, 'nll': 10.155213942394616}, 'chosen_samples': [100907, 54336, 30084, 40977, 76000], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.1453750080002, 'batch_acquisition_elapsed_time': 0.003142041999808498})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.29558510638297875, 'nll': 10.910028824801776}, 'chosen_samples': [76768, 625, 62170, 75168, 104154], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.296899950000125, 'batch_acquisition_elapsed_time': 0.002654074000020046})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3174468085106383, 'nll': 11.44309594489095}, 'chosen_samples': [20916, 108252, 54189, 48163, 104671], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.963882543999944, 'batch_acquisition_elapsed_time': 0.002789879999909317})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.31888297872340426, 'nll': 11.228596283023661}, 'chosen_samples': [69747, 7747, 29557, 11925, 26672], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.919115748000195, 'batch_acquisition_elapsed_time': 0.002828209999961473})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.35069148936170214, 'nll': 10.534543336458027}, 'chosen_samples': [98187, 69798, 69463, 24248, 111241], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.17242943200017, 'batch_acquisition_elapsed_time': 0.002972350000163715})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3421808510638298, 'nll': 9.906274580547148}, 'chosen_samples': [73837, 79098, 4926, 97912, 85915], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.49996366200003, 'batch_acquisition_elapsed_time': 0.002668677000201569})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3376595744680851, 'nll': 8.807538494154494}, 'chosen_samples': [39212, 12246, 45477, 48540, 53051], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 39.645957604999694, 'batch_acquisition_elapsed_time': 0.002832490999935544})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.366436170212766, 'nll': 9.65406924299547}, 'chosen_samples': [43456, 2543, 26823, 106192, 28643], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.70889785999998, 'batch_acquisition_elapsed_time': 0.002980304000175238})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3618085106382979, 'nll': 8.956222134652293}, 'chosen_samples': [88005, 103800, 92373, 10715, 76038], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.52361157300038, 'batch_acquisition_elapsed_time': 0.0027058900000156427})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3684574468085106, 'nll': 7.897528913874575}, 'chosen_samples': [36118, 52965, 10069, 48692, 60795], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.76154760700001, 'batch_acquisition_elapsed_time': 0.003064766000079544})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3725, 'nll': 7.974339260082614}, 'chosen_samples': [110391, 107606, 4214, 70556, 85243], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.78372856799979, 'batch_acquisition_elapsed_time': 0.0030976010002632393})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3852127659574468, 'nll': 7.29034953733708}, 'chosen_samples': [64036, 95709, 80772, 82801, 15338], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 41.267031723999935, 'batch_acquisition_elapsed_time': 0.0027807360002043424})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.36611702127659573, 'nll': 8.383804610032035}, 'chosen_samples': [43373, 24745, 56118, 44463, 39824], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 39.78458194399991, 'batch_acquisition_elapsed_time': 0.002998163000029308})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3829787234042553, 'nll': 7.322160244356761}, 'chosen_samples': [102692, 57531, 62197, 58392, 1892], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.66677778999974, 'batch_acquisition_elapsed_time': 0.0026175410002906574})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3854255319148936, 'nll': 7.793210487406306}, 'chosen_samples': [74680, 105865, 47421, 78221, 12503], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 38.698514437000085, 'batch_acquisition_elapsed_time': 0.0024795220001578855})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3822340425531915, 'nll': 7.125017186583674}, 'chosen_samples': [2719, 5057, 19308, 28507, 83062], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 39.94826357300008, 'batch_acquisition_elapsed_time': 0.0029825599999639962})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.38691489361702125, 'nll': 7.169642090522861}, 'chosen_samples': [67554, 28624, 38875, 91932, 97463], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 39.25612732400032, 'batch_acquisition_elapsed_time': 0.0027948940000896982})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.37670212765957445, 'nll': 7.682733356777657}, 'chosen_samples': [79675, 59443, 20484, 89666, 8881], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.71160082000006, 'batch_acquisition_elapsed_time': 0.0030939550001676253})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.3906914893617021, 'nll': 7.240681713630861}, 'chosen_samples': [109129, 112369, 89299, 81332, 79347], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 41.05701106400011, 'batch_acquisition_elapsed_time': 0.003034724999906757})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4123404255319149, 'nll': 7.356140906590731}, 'chosen_samples': [57946, 6299, 55647, 55955, 75042], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 41.293646956999964, 'batch_acquisition_elapsed_time': 0.002822019999712211})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4142021276595745, 'nll': 5.957098159033569}, 'chosen_samples': [102304, 28571, 75850, 20392, 57730], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.28472712800021, 'batch_acquisition_elapsed_time': 0.0028197689998705755})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.408031914893617, 'nll': 6.270738638732977}, 'chosen_samples': [111799, 7765, 71815, 16679, 100710], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.14540544600004, 'batch_acquisition_elapsed_time': 0.002790806999655615})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4165957446808511, 'nll': 6.333078362093009}, 'chosen_samples': [84458, 42417, 99404, 38683, 52495], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.1209646719999, 'batch_acquisition_elapsed_time': 0.0029533520000768476})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.40037234042553194, 'nll': 6.73572596654613}, 'chosen_samples': [51456, 79114, 101348, 94646, 338], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 39.88445423600024, 'batch_acquisition_elapsed_time': 0.00284062399987306})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.42898936170212765, 'nll': 5.400961729551248}, 'chosen_samples': [100797, 101335, 17202, 34041, 83887], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.50118877099976, 'batch_acquisition_elapsed_time': 0.002965413999845623})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.44468085106382976, 'nll': 5.588557259817072}, 'chosen_samples': [37695, 97067, 28329, 10403, 70], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.56015330700029, 'batch_acquisition_elapsed_time': 0.002750280999862298})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.46154255319148935, 'nll': 5.347817755269561}, 'chosen_samples': [101640, 94221, 55645, 30336, 7195], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 39.779190822000146, 'batch_acquisition_elapsed_time': 0.002477050000379677})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4631382978723404, 'nll': 5.094816195429006}, 'chosen_samples': [54525, 95829, 6589, 42862, 49091], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.179394996000156, 'batch_acquisition_elapsed_time': 0.0028724690000672126})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4656382978723404, 'nll': 5.029555365500616}, 'chosen_samples': [47576, 63623, 38830, 39337, 102149], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 39.47284222300004, 'batch_acquisition_elapsed_time': 0.002897790000133682})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.45595744680851064, 'nll': 5.203325023199333}, 'chosen_samples': [75494, 111771, 44411, 103994, 84608], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.17277633000003, 'batch_acquisition_elapsed_time': 0.0026529939996180474})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4696808510638298, 'nll': 5.075806741626338}, 'chosen_samples': [61256, 33147, 77376, 50750, 89081], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.32048949099999, 'batch_acquisition_elapsed_time': 0.0029497649998120323})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.46962765957446806, 'nll': 5.211826012806371}, 'chosen_samples': [109300, 55533, 55367, 103871, 17834], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.085333569999875, 'batch_acquisition_elapsed_time': 0.0026983650000147463})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4760106382978723, 'nll': 4.969583307368641}, 'chosen_samples': [12398, 99056, 66578, 58752, 63814], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 39.558470693000345, 'batch_acquisition_elapsed_time': 0.0028734729999086994})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4896276595744681, 'nll': 4.577623005229741}, 'chosen_samples': [98211, 109081, 31266, 51386, 39098], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 41.754797540000254, 'batch_acquisition_elapsed_time': 0.0027819590000035532})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4820212765957447, 'nll': 5.039650552616791}, 'chosen_samples': [52555, 109431, 38534, 30912, 31273], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 39.86402956699976, 'batch_acquisition_elapsed_time': 0.0028675949997705175})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4836170212765957, 'nll': 4.687810905114451}, 'chosen_samples': [701, 92463, 42053, 20503, 16155], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 40.76299006900035, 'batch_acquisition_elapsed_time': 0.0029827369999111397})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.4818085106382979, 'nll': 4.895271358891371}, 'chosen_samples': [66536, 80119, 98142, 31034, 89723], 'chosen_samples_score': [0.0, 0.0, 0.0, 0.0, 0.0], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 39.194004359000246, 'batch_acquisition_elapsed_time': 0.002722588999858999})