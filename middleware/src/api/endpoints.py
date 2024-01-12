# api/endpoints.py
from flask import request, jsonify
from utils.helpers import webscraper, ollama


def register_endpoints(app, get_services, save_service, get_service):
    @app.route('/api/v1/get-specs', methods=['GET'])
    def get_specs():
        name_param = request.args.get('name')
        
        # website = webscraper(name_param)

        website = """["","My Account","Canada","Graphics","MathWorksHelp CenterSearch","Get MATLABMATLABSign Into Your MathWorks AccountMy AccountMy Community ProfileLink LicenseSign Out","Italia(Italiano)","Netherlands(English)Norway(English)Österreich(Deutsch)Portugal(English)Sweden(English)SwitzerlandDeutschEnglishFrançaisUnited Kingdom(English)","Australia(English)India(English)New Zealand(English)中国简体中文ChineseEnglish日本Japanese(日本語)한국Korean(한국어)","Preventing Piracy","MathWorks is the leading developer of mathematical computing software for engineers and scientists.","Operating System","Français","My AccountMy Community ProfileLink LicenseSign Out","Select the China site (in Chinese or English) for best site performance. Other MathWorks country sites are not optimized for visits from your location.","Get MATLABMATLAB","(English)","Road Map","Newsroom","Select a Web SiteUnited StatesTrust CenterTrademarksPrivacy PolicyPreventing PiracyApplication Status© 1994-2024 The MathWorks, Inc.","Toggle Main Navigation","Help CenterHelp CenterMathWorksSearch","Storage","Finland(English)","United Kingdom","Belgium","ProductsSolutionsAcademiaSupportCommunityEvents","Videos and Webinars","(Français)","Sign Into Your MathWorks Account","América Latina","Select a Web SiteUnited StatesTrust CenterTrademarksPrivacy PolicyPreventing PiracyApplication Status© 1994-2024 The MathWorks, Inc.Join the conversation","Join the conversation","English","MATLABSimulinkStudent SoftwareHardware SupportFile Exchange","Deutschland","Search MathWorks.comMathWorksHelp CenterSearch","MATLAB","Toggle Main NavigationSign Into Your MathWorks AccountMy AccountMy Community ProfileLink LicenseSign OutProductsSolutionsAcademiaSupportCommunityEventsGet MATLABMATLAB","GPU acceleration using Parallel Computing Toolbox requires a GPU with a specific range of compute capability.  For more information, seeGPU Computing Requirements.","Help CenterHelp CenterMathWorksSearchSearch MathWorks.comMathWorksHelp CenterSearchClose Mobile Search","Finland","한국Korean","System Requirements","Training","Trust Center","Third-Party Compilers – Windows","Linux","Student Software","Search","Portugal","Contact your local office","MATLAB Interfaces to Other Languages","Try or Buy","Product Requirements","Mac","한국Korean(한국어)","Products","Norway","MathWorksAccelerating the pace of engineering and scienceMathWorks is the leading developer of mathematical computing software for engineers and scientists.Discover…","Korean","Operating SystemWindows 11Windows 10 (version 21H2 or higher)Windows Server 2019Windows Server 2022Note:Support for Windows Server 2019 will be discontinued in an upcoming releaseProcessorMinimum:Any Intel or AMD x86-64 processor with two or more coresRecommended:Any Intel or AMD x86-64 processor with four or more cores and AVX2 instruction set supportNote:A future release of MATLAB will require a processor with AVX2 instruction set supportRAMMinimum: 8 GBRecommended: 16 GBStorage3.8 GB for just MATLAB4-6 GB for a typical installation23 GB for an all products installationAn SSD is strongly recommendedGraphicsNo specific graphics card is required, but a hardware accelerated graphics card supporting OpenGL 3.3 with 1GB GPU memory is recommended.GPU acceleration using Parallel Computing Toolbox requires a GPU with a specific range of compute capability.  For more information, seeGPU Computing Requirements.","MATLAB Answers","System RequirementsWindowsMacLinuxBrowser RequirementsChoosing a ComputerUsing Previous MATLAB ReleasesProduct RequirementsSimulink RequirementsOther Product RequirementsMATLAB on Apple Silicon MacsThird-Party Compilers – WindowsThird-Party Compilers – MacThird-Party Compilers – LinuxMATLAB Interfaces to Other LanguagesRoad MapPrevious Releases","Toggle local navigation","Trial Software","You can also select a web site from the following list","Get SupportInstallation HelpMATLAB AnswersConsultingLicense CenterContact Support","MATLAB R2023b System Requirements for WindowsView Previous ReleasesOther Platforms:Mac|LinuxOperating SystemWindows 11Windows 10 (version 21H2 or higher)Windows Server 2019Windows Server 2022Note:Support for Windows Server 2019 will be discontinued in an upcoming releaseProcessorMinimum:Any Intel or AMD x86-64 processor with two or more coresRecommended:Any Intel or AMD x86-64 processor with four or more cores and AVX2 instruction set supportNote:A future release of MATLAB will require a processor with AVX2 instruction set supportRAMMinimum: 8 GBRecommended: 16 GBStorage3.8 GB for just MATLAB4-6 GB for a typical installation23 GB for an all products installationAn SSD is strongly recommendedGraphicsNo specific graphics card is required, but a hardware accelerated graphics card supporting OpenGL 3.3 with 1GB GPU memory is recommended.GPU acceleration using Parallel Computing Toolbox requires a GPU with a specific range of compute capability.  For more information, seeGPU Computing Requirements.","日本Japanese","Try or BuyDownloadsTrial SoftwareContact SalesPricing and LicensingHow to Buy","Processor","Installation HelpMATLAB AnswersConsultingLicense CenterContact Support","MATLAB on Apple Silicon Macs","Select a Web Site","MathWorksAccelerating the pace of engineering and scienceMathWorks is the leading developer of mathematical computing software for engineers and scientists.Discover…Explore ProductsMATLABSimulinkStudent SoftwareHardware SupportFile ExchangeTry or BuyDownloadsTrial SoftwareContact SalesPricing and LicensingHow to BuyLearn to UseDocumentationTutorialsExamplesVideos and WebinarsTrainingGet SupportInstallation HelpMATLAB AnswersConsultingLicense CenterContact SupportAbout MathWorksCareersNewsroomSocial MissionCustomer StoriesAbout MathWorks","Europe","Select a Web SiteUnited States","Trust CenterTrademarksPrivacy PolicyPreventing PiracyApplication Status","System RequirementsWindowsMacLinuxBrowser RequirementsChoosing a ComputerUsing Previous MATLAB Releases","Link License","DocumentationTutorialsExamplesVideos and WebinarsTraining","(Deutsch)","Minimum: 8 GBRecommended: 16 GB","How to Get Best Site PerformanceSelect the China site (in Chinese or English) for best site performance. Other MathWorks country sites are not optimized for visits from your location.","Belgium(English)","How to Get Best Site Performance","Documentation","Pricing and Licensing","GPU Computing Requirements","Hardware Support","About MathWorks","Contact Support","Sweden(English)","MathWorks","Asia Pacific","Denmark(English)","Österreich(Deutsch)","Ireland(English)","Installation Help","Previous Releases","Support","América Latina(Español)Canada(English)United States(English)","Choosing a Computer","MATLAB and Simulink RequirementsHelp CenterHelp CenterMathWorksSearchSearch MathWorks.comMathWorksHelp CenterSearchClose Mobile SearchClose Mobile SearchToggle local navigationSystem RequirementsWindowsMacLinuxBrowser RequirementsChoosing a ComputerUsing Previous MATLAB ReleasesProduct RequirementsSimulink RequirementsOther Product RequirementsMATLAB on Apple Silicon MacsThird-Party Compilers – WindowsThird-Party Compilers – MacThird-Party Compilers – LinuxMATLAB Interfaces to Other LanguagesRoad MapPrevious Releases","（简体中文）(English)","MATLAB and Simulink Requirements","简体中文Chinese","Application Status","简体中文ChineseEnglish","Windows","New Zealand","New Zealand(English)","License Center","×Select a Web SiteChoose a web site to get translated content where available and see local events and offers. Based on your location, we recommend that you select:.(English)(Deutsch)(Français)（简体中文）(English)You can also select a web site from the following listHow to Get Best Site PerformanceSelect the China site (in Chinese or English) for best site performance. Other MathWorks country sites are not optimized for visits from your location.AmericasAmérica Latina(Español)Canada(English)United States(English)EuropeBelgium(English)Denmark(English)Deutschland(Deutsch)España(Español)Finland(English)France(Français)Ireland(English)Italia(Italiano)Luxembourg(English)Netherlands(English)Norway(English)Österreich(Deutsch)Portugal(English)Sweden(English)SwitzerlandDeutschEnglishFrançaisUnited Kingdom(English)Asia PacificAustralia(English)India(English)New Zealand(English)中国简体中文ChineseEnglish日本Japanese(日本語)한국Korean(한국어)Contact your local office","Select a Web SiteChoose a web site to get translated content where available and see local events and offers. Based on your location, we recommend that you select:.(English)(Deutsch)(Français)（简体中文）(English)","MATLAB R2023b System Requirements for Windows","Luxembourg","France","Toggle local navigationSystem RequirementsWindowsMacLinuxBrowser RequirementsChoosing a ComputerUsing Previous MATLAB ReleasesProduct RequirementsSimulink RequirementsOther Product RequirementsMATLAB on Apple Silicon MacsThird-Party Compilers – WindowsThird-Party Compilers – MacThird-Party Compilers – LinuxMATLAB Interfaces to Other LanguagesRoad MapPrevious Releases","América Latina(Español)","© 1994-2024 The MathWorks, Inc.","Sign Into Your MathWorks AccountMy AccountMy Community ProfileLink LicenseSign OutProductsSolutionsAcademiaSupportCommunityEventsGet MATLABMATLAB","Events","日本Japanese(日本語)","（简体中文）","Australia","Chinese","Contact Sales","Discover…","DeutschEnglishFrançais","India(English)","AmericasAmérica Latina(Español)Canada(English)United States(English)","India","Explore Products","Simulink","Downloads","Sign Out","Help CenterMathWorksSearch","Consulting","to Your MathWorks Account","About MathWorksCareersNewsroomSocial MissionCustomer StoriesAbout MathWorks","Careers","Learn to Use","WindowsMacLinuxBrowser RequirementsChoosing a ComputerUsing Previous MATLAB Releases","Simulink Requirements","MathWorksAccelerating the pace of engineering and science","Product RequirementsSimulink RequirementsOther Product RequirementsMATLAB on Apple Silicon MacsThird-Party Compilers – WindowsThird-Party Compilers – MacThird-Party Compilers – LinuxMATLAB Interfaces to Other Languages","Explore ProductsMATLABSimulinkStudent SoftwareHardware SupportFile Exchange","Help CenterHelp CenterMathWorksSearchSearch MathWorks.comMathWorksHelp CenterSearch","España","Get MATLAB","Third-Party Compilers – Linux","Sweden","Note:Support for Windows Server 2019 will be discontinued in an upcoming release","Academia","MATLAB R2023b System Requirements for WindowsView Previous ReleasesOther Platforms:Mac|LinuxOperating SystemWindows 11Windows 10 (version 21H2 or higher)Windows Server 2019Windows Server 2022Note:Support for Windows Server 2019 will be discontinued in an upcoming releaseProcessorMinimum:Any Intel or AMD x86-64 processor with two or more coresRecommended:Any Intel or AMD x86-64 processor with four or more cores and AVX2 instruction set supportNote:A future release of MATLAB will require a processor with AVX2 instruction set supportRAMMinimum: 8 GBRecommended: 16 GBStorage3.8 GB for just MATLAB4-6 GB for a typical installation23 GB for an all products installationAn SSD is strongly recommendedGraphicsNo specific graphics card is required, but a hardware accelerated graphics card supporting OpenGL 3.3 with 1GB GPU memory is recommended.GPU acceleration using Parallel Computing Toolbox requires a GPU with a specific range of compute capability.  For more information, seeGPU Computing Requirements.×Select a Web SiteChoose a web site to get translated content where available and see local events and offers. Based on your location, we recommend that you select:.(English)(Deutsch)(Français)（简体中文）(English)You can also select a web site from the following listHow to Get Best Site PerformanceSelect the China site (in Chinese or English) for best site performance. Other MathWorks country sites are not optimized for visits from your location.AmericasAmérica Latina(Español)Canada(English)United States(English)EuropeBelgium(English)Denmark(English)Deutschland(Deutsch)España(Español)Finland(English)France(Français)Ireland(English)Italia(Italiano)Luxembourg(English)Netherlands(English)Norway(English)Österreich(Deutsch)Portugal(English)Sweden(English)SwitzerlandDeutschEnglishFrançaisUnited Kingdom(English)Asia PacificAustralia(English)India(English)New Zealand(English)中国简体中文ChineseEnglish日本Japanese(日本語)한국Korean(한국어)Contact your local office","Denmark","Privacy Policy","Choose a web site to get translated content where available and see local events and offers. Based on your location, we recommend that you select:.","Belgium(English)Denmark(English)Deutschland(Deutsch)España(Español)Finland(English)France(Français)Ireland(English)Italia(Italiano)Luxembourg(English)Netherlands(English)Norway(English)Österreich(Deutsch)Portugal(English)Sweden(English)SwitzerlandDeutschEnglishFrançaisUnited Kingdom(English)","×","United States(English)","Deutsch","Netherlands(English)","Americas","Deutschland(Deutsch)","United States","Österreich","CareersNewsroomSocial MissionCustomer StoriesAbout MathWorks","Using Previous MATLAB Releases","RAM","DownloadsTrial SoftwareContact SalesPricing and LicensingHow to Buy","Close Mobile Search","Italia","Community","Canada(English)","Customer Stories","ProductsSolutionsAcademiaSupportCommunityEventsGet MATLABMATLABSign Into Your MathWorks AccountMy AccountMy Community ProfileLink LicenseSign Out","Japanese","Australia(English)","Get Support","Select a Web SiteChoose a web site to get translated content where available and see local events and offers. Based on your location, we recommend that you select:.(English)(Deutsch)(Français)（简体中文）(English)You can also select a web site from the following listHow to Get Best Site PerformanceSelect the China site (in Chinese or English) for best site performance. Other MathWorks country sites are not optimized for visits from your location.AmericasAmérica Latina(Español)Canada(English)United States(English)EuropeBelgium(English)Denmark(English)Deutschland(Deutsch)España(Español)Finland(English)France(Français)Ireland(English)Italia(Italiano)Luxembourg(English)Netherlands(English)Norway(English)Österreich(Deutsch)Portugal(English)Sweden(English)SwitzerlandDeutschEnglishFrançaisUnited Kingdom(English)Asia PacificAustralia(English)India(English)New Zealand(English)中国简体中文ChineseEnglish日本Japanese(日本語)한국Korean(한국어)Contact your local office","Trademarks","France(Français)","Windows 11Windows 10 (version 21H2 or higher)Windows Server 2019Windows Server 2022","Portugal(English)","My Community Profile","Accelerating the pace of engineering and science","Ireland","Third-Party Compilers – Mac","Browser Requirements","Learn to UseDocumentationTutorialsExamplesVideos and WebinarsTraining","Norway(English)","Netherlands","Simulink RequirementsOther Product RequirementsMATLAB on Apple Silicon MacsThird-Party Compilers – WindowsThird-Party Compilers – MacThird-Party Compilers – LinuxMATLAB Interfaces to Other Languages","Luxembourg(English)","Tutorials","How to Buy","(English)(Deutsch)(Français)","Solutions","View Previous Releases","Skip to content","No specific graphics card is required, but a hardware accelerated graphics card supporting OpenGL 3.3 with 1GB GPU memory is recommended.","中国简体中文ChineseEnglish","Asia PacificAustralia(English)India(English)New Zealand(English)中国简体中文ChineseEnglish日本Japanese(日本語)한국Korean(한국어)","File Exchange","Other Platforms:Mac|Linux","MATLAB and Simulink RequirementsHelp CenterHelp CenterMathWorksSearchSearch MathWorks.comMathWorksHelp CenterSearchClose Mobile SearchClose Mobile Search","Belgium(English)Denmark(English)Deutschland(Deutsch)España(Español)Finland(English)France(Français)Ireland(English)Italia(Italiano)Luxembourg(English)","United Kingdom(English)","EuropeBelgium(English)Denmark(English)Deutschland(Deutsch)España(Español)Finland(English)France(Français)Ireland(English)Italia(Italiano)Luxembourg(English)Netherlands(English)Norway(English)Österreich(Deutsch)Portugal(English)Sweden(English)SwitzerlandDeutschEnglishFrançaisUnited Kingdom(English)","Other Product Requirements","SwitzerlandDeutschEnglishFrançais","Social Mission","AmericasAmérica Latina(Español)Canada(English)United States(English)EuropeBelgium(English)Denmark(English)Deutschland(Deutsch)España(Español)Finland(English)France(Français)Ireland(English)Italia(Italiano)Luxembourg(English)Netherlands(English)Norway(English)Österreich(Deutsch)Portugal(English)Sweden(English)SwitzerlandDeutschEnglishFrançaisUnited Kingdom(English)Asia PacificAustralia(English)India(English)New Zealand(English)中国简体中文ChineseEnglish日本Japanese(日本語)한국Korean(한국어)","Examples","España(Español)","Explore ProductsMATLABSimulinkStudent SoftwareHardware SupportFile ExchangeTry or BuyDownloadsTrial SoftwareContact SalesPricing and LicensingHow to BuyLearn to UseDocumentationTutorialsExamplesVideos and WebinarsTrainingGet SupportInstallation HelpMATLAB AnswersConsultingLicense CenterContact SupportAbout MathWorksCareersNewsroomSocial MissionCustomer StoriesAbout MathWorks","Help Center","3.8 GB for just MATLAB4-6 GB for a typical installation23 GB for an all products installationAn SSD is strongly recommended"]"""

        component_response = ollama(website)
        if component_response:
            # save_service(component_response['service_name'], component_response['json_data'])
            return jsonify({'message': component_response})

        return jsonify({'error': 'Servizio non trovato e impossibile ottenere i dati dal componente'}), 404

    
    @app.route('/api/v1/get-services', methods=['GET'])
    def get_all_services():
        return get_services()