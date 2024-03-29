from zope.interface import Interface
from zope.interface import directlyProvides
from zope.interface import Attribute
from zope.viewlet.interfaces import IViewletManager
from zope.contentprovider.interfaces import ITALNamespaceData


class IIssueFolderView(Interface):
    """Abstract a PoiTracker into a folder for issues.
    """

    def getFilteredIssues(criteria, **kwargs):
        """Get the contained issues in the given criteria.
        """

    def getIssueSearchQueryString(criteria, **kwargs):
        """Return a query string for an issue query.
        """

    def buildIssueSearchQuery(criteria, **kwargs):
        """Build canonical query for issue search.
        """

    def getMyIssues(openStates, memberId, manager):
        """Get a catalog query result set of my issues.

        So: all issues assigned to or submitted by the current user,
        with review state in openStates.

        If manager is True, you can add more states.
        """

    def getOrphanedIssues(openStates, memberId):
        """Get a catalog query result set of orphaned issues.

        Meaning: all open issues not assigned to anyone and not owned
        by the given user.
        """

    def getPressureForIssue(issue):
        """Calculates the pressure of an issue on its brain.
        
        Returns an integer as pressure state:
            1: Overdue
            2: Needs to be worked on today
            3: Still time left
        """

class IResponseAdder(IViewletManager):

    mimetype = Attribute("Mime type for response.")
    use_wysiwyg = Attribute("Boolean: Use kupu-like editor.")

    def transitions_for_display():
        """Get the available transitions for this issue.
        """

    def severities_for_display():
        """Get the available severities for this issue.
        """

    def releases_for_display():
        """Get the releases from the project.
        """

    def managers_for_display():
        """Get the tracker managers.
        """

directlyProvides(IResponseAdder, ITALNamespaceData)


class ICreateResponse(Interface):
    pass
